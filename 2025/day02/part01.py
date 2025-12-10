#!/usr/bin/env python3

# Advent of Code 2025 Day 2 Part 1 Solution

import os

def sum_invalid_ids_in_range(start: int, end: int) -> int:
  """
    Calculates the sum of all invalid IDs within a given inclusive range.

    An invalid ID is defined as a number that consists of a digit sequence
    repeated exactly twice (e.g., 55, 6464, 123123). The number must not
    contain leading zeros. This function efficiently detects all such
    repeated-sequence numbers without iterating through each value.

    :param start: The beginning of the range (inclusive).
    :param end: The end of the range (inclusive).

    :return total: The sum of all invalid IDs found within the range.
    """
  if start > end:
    return 0

  total = 0
  max_digits = len(str(end))
  max_half_length = max_digits // 2

  for half_len in range(1, max_half_length + 1):
    multiplier = 10 ** half_len + 1  # Example: 12 → 1212

    min_seq = 10 ** (half_len - 1)
    max_seq = 10 ** half_len - 1

    seq_start = (start + multiplier - 1) // multiplier
    seq_end = end // multiplier

    left = max(seq_start, min_seq)
    right = min(seq_end, max_seq)

    if left <= right:
      count = right - left + 1
      sequence_sum = (left + right) * count // 2
      total += multiplier * sequence_sum

  return total


def sum_invalid_ids_from_ranges(range_string: str) -> int:
  """
    Calculates the total sum of all invalid IDs from a comma-separated
    list of numeric ranges.

    Each range must follow the format:
    start-end

    Example:
    "11-22,95-115,998-1012"

    :param range_string: A single-line comma-separated string of numeric ranges.

    :return total: The total sum of all invalid IDs across all ranges.
    """
  total = 0
  ranges = [r.strip() for r in range_string.split(",") if r.strip()]

  for r in ranges:
    start_str, end_str = r.split("-")
    start = int(start_str)
    end = int(end_str)

    total += sum_invalid_ids_in_range(start, end)

  return total


def sum_invalid_ids_from_file(file_path: str) -> int:
  """
    Calculates the total sum of all invalid IDs from a text file
    containing a single line of comma-separated numeric ranges.

    Example file content:
    11-22,95-115,998-1012

    :param file_path: Path to the input text file.

    :return total: The total sum of all invalid IDs across all ranges in the file.
    """
  with open(file_path, "r", encoding="utf-8") as file:
    range_string = file.readline().strip()

  total = sum_invalid_ids_from_ranges(range_string)

  return total

def main():
  '''Program Entry Point'''

  dirname = os.path.dirname(__file__)
  INPUT_FILE = os.path.join(dirname, "input.txt")

  total = sum_invalid_ids_from_file(INPUT_FILE)
  print("Total Invalid ID Sum:", total)

# Program Entry Point
if __name__ == "__main__":
  main()

