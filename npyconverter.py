# File locations
NPY_DATA_PATH = "data/data-npy"
CLEAN_DATA_PATH = "data/data-npy-clean"
TXT_DATA_PATH = "data/data-txt"
TSV_DATA_PATH = "data/data-tsv"

import numpy as np
import os
import re
import csv


def find_npy_files(path):
    """
    Finds all npy files and terminal folders in a given path
    :param path: path to search
    :return: list of npy files paths
    """
    npy_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".npy"):
                npy_files.append(os.path.join(root, file))
    return npy_files


def remove_lines(string):
    """
    Do a little clean up on the string:
    1. remove new lines
    2. remove double spaces
    3. remove non-breaking spaces
    4. remove leading spaces
    5. remove trailing spaces
    6. remove trailing commas
    7. remove period + comma
    TODO:
    3. fix typos?
    """
    if isinstance(string, str):
        string = string.replace("\n", "")
        string = string.replace("\xa0", " ")
        string = string.replace("  ", " ")
        string = string.replace(".,", ";;")
        if string.startswith(" "):
            string = string[1:]
        if string.endswith(" "):
            string = string[:-1]
        if string.endswith(","):
            string = string[:-1]
        return string
    elif isinstance(string, list):
        return [remove_lines(x) for x in string]
    else:
        return str(string)


def npy_to_txt(npy_path, txt_path):
    """
    Converts npy files to txt files
    :param npy_path: path to npy files
    :param txt_path: path to save txt files
    """
    npy = np.load(npy_path, allow_pickle=True)
    with open(txt_path, 'w') as f:
        for i in range(len(npy)):
            f.write("Question " + str(i+1) + ":\n")
            for key in npy[i]:
                f.write(remove_lines(key) + ": ")
                if isinstance(npy[i][key], list):
                    line = "".join(str(x) + ", " for x in npy[i][key])
                    f.write(remove_lines(line) + "\n")
                else:
                    f.write(remove_lines(npy[i][key]) + "\n")
            f.write("\n\n")


def npy_to_tsv(npy_path, tsv_path):
    """
    Converts npy files to tsv files
    :param npy_path: path to npy files
    :param tsv_path: path to save tsv files
    """
    npy = np.load(npy_path, allow_pickle=True)
    with open(tsv_path, "wt") as outfile:
        tsv_writer = csv.writer(outfile, delimiter="\t")
        header = []
        for key in npy[0]:
            header.append(remove_lines(key))
        tsv_writer.writerow(header)
        for i in range(len(npy)):
            row = []
            for key in npy[i]:
                if isinstance(npy[i][key], list):
                    line = "".join(str(x) + ", " for x in npy[i][key])
                    row.append(remove_lines(line))
                else:
                    row.append(remove_lines(npy[i][key]))
            tsv_writer.writerow(row)


def clean_npy(npy_path):
    """
    Clean up the npy file with remove_lines()
    """
    npy = np.load(npy_path, allow_pickle=True)
    save_path = re.sub(r"data-npy", "data-npy-clean", npy_path)
    for i in range(len(npy)):
        for key in npy[i]:
            if isinstance(npy[i][key], list):
                npy[i][key] = [remove_lines(x) for x in npy[i][key]]
            else:
                npy[i][key] = remove_lines(npy[i][key])
    np.save(save_path, npy, allow_pickle=True)


def main():
    for file in find_npy_files(NPY_DATA_PATH):
        txt_path = re.sub(r"npy", "txt", file)
        tsv_path = re.sub(r"npy", "tsv", file)
        npy_to_txt(file, txt_path)
        npy_to_tsv(file, tsv_path)
        clean_npy(file)


if __name__ == "__main__":
    main()