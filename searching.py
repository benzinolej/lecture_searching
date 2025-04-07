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

def patter_search(seq, patt):
    ...

def main():
    file_name = "sequential.json"
    #raed data
    seq = read_data(file_name, field="unordered_numbers")
    print(seq)

if __name__ == '__main__':
    main()