#!/usr/bin/env python3

# Advent of Code 2024 Day 1 Part 2 Solution

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

def find_similarity_score(left_list, right_list):
    """
    Computes the similarity score between two lists by summing the product
    of each element in the left list and the number of times that element
    appears in the right list.

    :param left_list: A list of integers.
    :param right_list: A list of integers.

    :return: The similarity score, an integer representing the total sum
             of products as described.
    """
    sum_similarity_score = 0;

    for i in range(len(left_list)):
        similarity_count = 0
        for j in range(len(right_list)):
            if left_list[i] == right_list[j]:
                similarity_count += 1
        sum_similarity_score += similarity_count * left_list[i]

    return sum_similarity_score


def main():
    """
    Reads the input.txt file, extracts the left and right lists, and
    computes the similarity score of the two lists by multiplying the
    number of times each element appears in the other list by the
    element itself.

    Prints the similarity score to the console.

    :return: None
    """
    dirname = os.path.dirname(__file__)
    data = os.path.join(dirname, "input.txt")
    left_list = []
    right_list = []
    similarity_score = 0

    left_list, right_list = extract_left_right_list(data)

    similarity_score = find_similarity_score(left_list, right_list)
    print(similarity_score)


if __name__ == "__main__":
    main()