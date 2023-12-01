# File locations
NPY_DATA_PATH = "data/data-npy"
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
    if isinstance(string, str):
        return string.replace('\n', ' ')
    else:
        return string


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
                    for val in npy[i][key]:
                        f.write(str(remove_lines(val)) + ", ")
                    f.write("\n")
                else:
                    f.write(str(remove_lines(npy[i][key])) + "\n")
            f.write("\n")


def npy_to_tsv(npy_path, tsv_path):
    """
    Converts npy files to tsv files
    :param npy_path: path to npy files
    :param tsv_path: path to save tsv files
    """
    npy = np.load(npy_path, allow_pickle=True)
    with open(tsv_path, 'wt') as f:
        tsv_writer = csv.writer(tsv_path, delimiter='\t')
        header = []
        for key in npy[0]:
            header.append(key)
        tsv_writer.writerow(header)
        for i in range(len(npy)):
            row = []
            for key in npy[i]:
                if isinstance(npy[i][key], list):
                    row.append(", ".join(npy[i][key]))
                else:
                    row.append(npy[i][key])
            tsv_writer.writerow(row)


def main():
    for file in find_npy_files(NPY_DATA_PATH):
        txt_path = re.sub(r"npy", "txt", file)
        tsv_path = re.sub(r"npy", "tsv", file)
        npy_to_txt(file, txt_path)
        npy_to_tsv(file, tsv_path)


if __name__ == "__main__":
    main()