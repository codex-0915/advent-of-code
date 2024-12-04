#!/usr/bin/env python3

# Advent of Code 2024 Day 1 Part 1 Solution

import os

def extract_left_right_list(data):
    """
    Extracts the left and right lists from the given file.

    The file is expected to have one number per line, with the left number
    appearing first and the right number appearing second.

    :param data: The file to read from

    :return: A tuple of two lists, the left list and the right list
    """
    left = []
    right = []

    with open(data) as file:
        for line in file:
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))
    return left, right

def get_sorted_distance_sum(left_list, right_list):
    """
    Calculates the sum of absolute differences between corresponding elements
    of two sorted lists.

    The function first sorts the given left and right lists, then computes
    the sum of absolute differences between each pair of elements at the
    same index in the sorted lists.

    :param left_list: The first list of integers.
    :param right_list: The second list of integers.

    :return: The sum of absolute differences between the sorted lists.
    """
    sorted_distance_sum = 0;
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)

    for i in range(len(left_list)):
        sorted_distance_sum += abs(sorted_left_list[i] - sorted_right_list[i])

    return sorted_distance_sum


def main():
    """
    Reads the input.txt file and prints the sum of absolute differences between
    the sorted elements of the left and right lists.

    The input.txt file is expected to have one number per line, with the left
    number appearing first and the right number appearing second.

    :return: None
    """
    dirname = os.path.dirname(__file__)
    data = os.path.join(dirname, "input.txt")
    left_list = []
    right_list = []
    distance_sum = 0

    left_list, right_list = extract_left_right_list(data)

    distance_sum = get_sorted_distance_sum(left_list, right_list)
    print(distance_sum)


if __name__ == "__main__":
    main()