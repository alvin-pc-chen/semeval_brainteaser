import os
from numpy import logical_and, sum as t_sum
import numpy as np
from pathlib import Path
from typing import List
import random
from datetime import datetime
from openai import OpenAI
import prompts

# File locations
ROOTDIR = str(Path().parent.absolute().parent.absolute())
NPY_DATA_PATH = ROOTDIR + "/data/data-npy"
CLEAN_DATA_PATH = ROOTDIR + "/data/data-npy-clean"
TXT_DATA_PATH = ROOTDIR + "/data/data-txt"
TSV_DATA_PATH = ROOTDIR + "/data/data-tsv"
WORKING_DIR = CLEAN_DATA_PATH + "/all-data-new"
TEST_LOGS = ROOTDIR + "/testing/test_logs"


def load_data(path=WORKING_DIR):
    """
    Load data from path
    :param path: path to data
    :return: list of data, dictionary of index to names
    """
    data = []
    key = {}
    docnum = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".npy"):
                data.append(np.load(os.path.join(root, file), allow_pickle=True))
                key[docnum] = str(file)
                docnum += 1
    for i in range(len(data)):
        print(f"Loaded {key[i]} at index {i}")
    return data, key


def split_data(data, split=0.8):
    random.shuffle(data)
    split_index = int(len(data) * split)
    return data[:split_index], data[split_index:]


def split_data_by_type(data):
    """
    Split data into base, sr, and cr
    """
    sr = []
    cr = []
    base = []
    for d in data:
        if "SR" in d["id"]:
            sr.append(d)
        elif "CR" in d["id"]:
            cr.append(d)
        else:
            base.append(d)
    return base, sr, cr



# Testing starts here
def log_results(
        answers,
        wrong_answers,
        ids,
        model,
        f1,
        accuracy,
        question_prompt,
        system_prompt,
        n,
        m,
        dataset,
        training_data,
        version,
        path=TEST_LOGS):
    """
    Header: timestamp, model, version, statistics, prompts
    Body: question, correct answer, model answer
    """
    time = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    name = model + "_" + version + "_" + time
    if training_data is not None:
        name += "_multishot"
    with open(f"{path}/{name}.log", "a") as f:
        # Write header
        f.write(f"Created: {time}\n")
        f.write(f"Model: {model}, Version: {version}\n")
        f.write(f"Number of Questions: {n}, Number of Examples: {m}, Number of Bad Outputs: {len(wrong_answers)}\n")
        f.write(f"F1: {f1}, Accuracy: {accuracy}\n")
        f.write(f"System Prompt: {system_prompt}\n")
        f.write(f"User Prompt: {question_prompt}\n\n\n")
        # Write question, correct answer, model answer
        for i in range(n):
            f.write(f"Question {ids[i]}: {dataset[i]['question']}\n")
            if ids[i] in wrong_answers:
                f.write(f"Model Answer (Wrong): {wrong_answers[ids[i]]}\n")
            else:
                f.write(f"Model Answer: {dataset[i]['choice_list'][answers[i]]}\n")
            f.write(f"Correct Answer: {dataset[i]['answer']}\n\n")


def generate_prompt(question, prefix):
    choices = "".join(str(i) + " = " + question["choice_list"][i] + "; " for i in range(4))
    content = prefix + "\"" + question["question"] + "\"\nChoices: " + choices + "\nResponse: "
    return {"role": "user", "content": content}


def multishot_prompt(training, prefix):
    prompt = prefix
    for i in range(len(training)):
        choices = "".join(str(j) + " = " + training[i]["choice_list"][j] + "; " for j in range(4))
        prompt += "Question: "+"\""+ training[i]["question"] +"\"\nChoices: "+ choices +"\nResponse: "+ training[i]["label"] +"\n"
    return {"role": "system", "content": prompt}


# Testing for GPT
# Model settings
MODEL = "gpt-3.5-turbo"
SYSTEM_PROMPT = {"role": "system", 
                 "content": "You are a Question Answering Model, \
                your response must be a number from the choices that are delimited by the symbol \";\" ."}
MULTI_PREFIX = "You are a Question Answering Model, \
                your response must be a number from the choices that are delimited by the symbol \";\". \
                Here are some examples: \n"
SP_QUESTION = "Think outside of the box and respond with the number corresponding to the best choice for the \
                following question.\n\nQuestion: "
WP_QUESTION = "For the following word problem, look at the meaning and letters in the words and respond with the \
                number corresponding to the best choice.\n\nQuestion: "
def run_test_nofinetune(
            client,
            dataset,
            question_prompt,
            n=30,
            training_data=None,
            m=10,
            model=MODEL,
            version="0",
            system_prompt=SYSTEM_PROMPT,
            multi_prefix=MULTI_PREFIX,
            classes=[0, 1, 2, 3],):
    """
    Dataset is a list of dicts, each dict contains question, choices, and answer
    training_data either none or list of training data
    n is the number of questions to test
    m is the number of training examples to use
    no finetuning means some outputs may not be ints, non-ints will be set as incorrect answer
    return avg f1 score
    """
    answers = []
    labels = []
    ids = []
    wrong_answers = {}
    count = 0
    # Randomize dataset
    random.shuffle(dataset)
    if training_data is not None:
        random.shuffle(training_data)
    # Run test
    for i in range(n):
        user_prompt = generate_prompt(dataset[i], question_prompt)
        if training_data is not None:
            first_prompt = multishot_prompt(training_data[:m], multi_prefix)
        else:
            first_prompt = system_prompt
            m = 0
        prompt = [first_prompt, user_prompt]
        response = client.chat.completions.create(model=model, messages=prompt)
        ans = response.choices[0].message.content
        if ans in ["0", "1", "2", "3"]:
            answers.append(int(ans))
        elif dataset[i]["label"] == 0:
            answers.append(1)
            wrong_answers[dataset[i]["id"]] = ans
        else:
            answers.append(0)
            wrong_answers[dataset[i]["id"]] = ans
        labels.append(int(dataset[i]["label"]))
        ids.append(dataset[i]["id"])
        # Manual Accuracy
        if answers[i] == labels[i]:
            count += 1
    # Get F1 and Accuracy
    f1 = avg_f1_score(answers, labels, classes)
    acc = count/n
    # Log results
    log_results(
        answers,
        wrong_answers,
        ids,
        model,
        f1,
        acc,
        question_prompt,
        first_prompt['content'],
        n,
        m,
        dataset[:n],
        training_data,
        version,
    )
    return f1, acc


# Make finetune testing


# F1 starts here
def accuracy(predicted_labels: List[int], true_labels: List[int]):
    """
    Accuracy is correct predictions / all predicitons
    """
    correct_count = 0
    for pred, label in zip(predicted_labels, true_labels):
        correct_count += int(pred == label)

    return correct_count/len(true_labels) if len(true_labels) > 0 else 0.


def precision(predicted_labels, true_labels, which_label=1):
    """
    Precision is True Positives / All Positives Predictions
    """
    pred_which = np.array([pred == which_label for pred in predicted_labels])
    true_which = np.array([lab == which_label for lab in true_labels])
    denominator = t_sum(pred_which)
    if denominator:
        return t_sum(logical_and(pred_which, true_which))/denominator
    else:
        return 0.


def recall(predicted_labels, true_labels, which_label=1):
    """
    Recall is True Positives / All Positive Labels
    """
    pred_which = np.array([pred == which_label for pred in predicted_labels])
    true_which = np.array([lab == which_label for lab in true_labels])
    denominator = t_sum(true_which)
    if denominator:
        return t_sum(logical_and(pred_which, true_which))/denominator
    else:
        return 0.


def f1_score(predicted_labels, true_labels, which_label=1):
    """
    F1 score is the harmonic mean of precision and recall
    """
    P = precision(predicted_labels, true_labels, which_label=which_label)
    R = recall(predicted_labels, true_labels, which_label=which_label)
    if P and R:
        return 2*P*R/(P+R)
    else:
        return 0.


def avg_f1_score(predicted_labels: List[int], true_labels: List[int], classes: List[int]):
    """
    Calculate the f1-score for each class and return the average of it
    """
    return sum([f1_score(predicted_labels, true_labels, which_label=which_label) for which_label in classes])/len(classes)