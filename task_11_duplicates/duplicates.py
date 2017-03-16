import filecmp
import os
import itertools
import sys


def compare_files(file_path1, file_path_2):
    if filecmp.cmp(file_path1, file_path_2):
        return True
    return False

if __name__ == '__main__':
    root_catalog = sys.argv[1]
    files_list = []

    print(os.walk(root_catalog))
    for paths, dirs, files in os.walk(root_catalog):
        # print(files)
        for file_name in files:
            files_list.append(os.path.join(paths, file_name))
    # print(files_list)

    for file1, file2 in itertools.combinations(files_list, 2):
        if compare_files(file1, file2):
            print("Duplicate files found: First file - {} and second file - {}".format(file1, file2))
