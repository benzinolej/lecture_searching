import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    #file_path = os.path.join(cwd_path, file_name)

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        sequentional_data = json.load(json_file)

    return sequentional_data

def linear_search(seq, number):
    """
    :param seq:
    :param number:
    :return:
    """
    indices = []
    count = 0
    idx =0
    while idx < len(seq):
        if seq[idx] == number:
            indices.append(idx)
            count += 1
        idx += 1
    return {"positions": indices, "count": count}

def pattern_search(seq, patt):
    patt_size = len(patt)
    f_idx = 0
    s_idx = patt_size

    while s_idx < len(seq):
        for idx in range(patt_size):
            if pattern[idx] != seq[f_idx + idx]:
                break
        else:
            indices.add(f_idx + patt_size // 2)
        f_idx += 1
        s_idx += 1

        return indices

def binary_search(ordered_list, number):
    left, right = (0, len(seq) - 1)
    while left <= right:
        middle = (right + left) // 2

        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            return middle


def main():
    file_name = "sequential.json"
    #raed data
    seq = read_data(file_name, field="unordered_numbers")

    result = linear_search(seq, number=0)

    seq = pattern_search(file_name, field= "one_sequence")

if __name__ == '__main__':
    main()