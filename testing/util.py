import os
from numpy import logical_and, sum as t_sum
import numpy as np
from pathlib import Path
from typing import List
import random
from datetime import datetime

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
    """
    Split data into training and testing sets
    :param data: list of data
    :param split: percentage of data to use for training
    :return: training and testing sets
    """
    random.shuffle(data)
    split_index = int(len(data) * split)
    return data[:split_index], data[split_index:]


def split_data_by_type(data, split=0.8):
    """
    Split train/dev sets by type, only run on train data
    :param data: list of dict
    :param split: dev/train split
    :return: base data train/dev, sr data train/dev, cr data train/dev
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
    return split_data(base, split), split_data(sr, split), split_data(cr, split)


def log_results(results, name, path=TEST_LOGS):
    """
    Log results to file
    :param results: header with model name, time, prompt information, etc.
    :param name: name of model
    :param path: path to log file
    """
    with open(f"{path}/{name}.log", "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for r in results:
            f.write(f"{r}\n")
        f.write("\n")


def accuracy(predicted_labels, true_labels):
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