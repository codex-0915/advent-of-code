#!/usr/bin/env python3

# Advent of Code 2024 Day 2 Part 1 Solution

import os

def count_safe_reports(data_reports):
    """
    Counts the number of safe reports in the given data file.

    A report is considered safe if the array of numbers in each line is
    either strictly increasing or strictly decreasing with differences
    between consecutive elements between 1 and 3 inclusive.

    :param data_reports: The path to the file containing the reports.
    :return: The count of safe reports.
    """
    safe_reports = 0

    # Open the file and iterate through each line
    with open(data_reports) as file:
        for line in file:
            # Convert the line into a list of integers
            line_report = list(map(int, line.split()))
            
            # Check if the current line report is safe
            if check_safe_report(line_report):
                safe_reports += 1

    return safe_reports

def check_safe_report(array_data):
    """
    Checks if the given array of data is safe. The array is considered safe
    if it is either strictly increasing or strictly decreasing and the
    difference between consecutive elements is between 1 and 3 (inclusive).
    """
    is_increasing = False
    is_decreasing = False
    diff = 0
    is_report_safe = False

    # Check if the elements from the start of the array until the end 
    # are either all increasing or all decreasing
    is_increasing = all(array_data[i] < array_data[i+1] for i in range(len(array_data)-1))
    is_decreasing = all(array_data[i] > array_data[i+1] for i in range(len(array_data)-1))

    if is_increasing or is_decreasing:
        i = 0
        is_report_safe = True
        while i <= len(array_data)-2 and is_report_safe == True:
            # Take the absolute difference between the current element and
            # the previous element
            diff = abs(array_data[i+1] - array_data[i])

            # Check if the difference is between 1 and 3 (inclusive)
            if diff >= 1 and diff <= 3:
                is_report_safe = True
            else:
                is_report_safe = False
            i += 1
    else:
        is_report_safe = False

    return is_report_safe

# def extract_array_from_line_report(data):
#     array = []
#     with open(data) as file:
#         for line in file:
#             array.append(line.split())
#     return array

def main():
    """
    The main entry point of the program.

    This function calls the count_safe_reports() function to count the
    number of safe reports in the input.txt file and prints the result.
    """
    dirname = os.path.dirname(__file__)
    input_data = os.path.join(dirname, "input.txt")
    total_safe_reports = 0

    # Count the number of safe reports in the input.txt file
    total_safe_reports = count_safe_reports(input_data)

    # Print the total number of safe reports
    print(total_safe_reports)

if __name__ == "__main__":
    main()