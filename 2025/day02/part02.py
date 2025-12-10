#!/usr/bin/env python3

# Advent of Code 2025 Day 2 Part 2 Solution

import os

def _is_primitive_str(s: str) -> bool:
  """
    Checks whether the given digit string is primitive (not made by
    repeating a smaller substring).

    :param s: The digit string to check.

    :return: True if s is primitive, False otherwise.
    """
  L = len(s)
  for k in range(1, L // 2 + 1):
    if L % k == 0:
      if s == s[:k] * (L // k):
        return False
  return True


def _generate_invalid_ids_in_bounds(min_value: int, max_value: int) -> set:
  """
    Generates all invalid IDs in the inclusive interval [min_value, max_value].
    An invalid ID is a number that equals a primitive digit-sequence repeated
    at least twice (e.g., 123123, 1111111, 1212121212). Each invalid ID is
    produced exactly once.

    This function enumerates primitive base lengths p and repetition counts
    reps (>=2) such that the total digits p*reps do not exceed the number of
    digits of max_value. For each eligible primitive base sequence of length p,
    it constructs the repeated number and includes it if within bounds.

    :param min_value: Lower bound of search (inclusive).
    :param max_value: Upper bound of search (inclusive).

    :return: A set of integers representing all invalid IDs within the bounds.
    """
  if min_value > max_value:
    return set()

  invalid = set()
  max_digits = len(str(max_value))

  for p in range(1, max_digits + 1):
    seq_lo = 10 ** (p - 1)
    seq_hi = 10 ** p - 1
    max_reps = max_digits // p
    if max_reps < 2:
      continue
    pow_p = 10 ** p
    for reps in range(2, max_reps + 1):
      # multiplier = 1 + 10^p + 10^(2p) + ... + 10^{(reps-1)*p}
      multiplier = (10 ** (p * reps) - 1) // (pow_p - 1)
      lo = (min_value + multiplier - 1) // multiplier
      hi = max_value // multiplier
      lo = max(lo, seq_lo)
      hi = min(hi, seq_hi)
      if lo > hi:
        continue
      for seq in range(lo, hi + 1):
        s = str(seq)
        if _is_primitive_str(s):
          n = seq * multiplier
          # extra safety: ensure the final number's digit-length equals p*reps
          if len(str(n)) == p * reps:
            invalid.add(n)

  return invalid


def sum_invalid_ids_from_ranges(range_string: str) -> int:
  """
    Calculates the total sum of all invalid IDs from a comma-separated
    list of numeric ranges. The implementation generates all invalid IDs
    within the global bounds of the input ranges, then sums those that
    fall into each range (avoiding duplicate counting).

    :param range_string: A single-line comma-separated string of numeric ranges.

    :return: The total sum of all invalid IDs across all ranges.
    """
  parts = [p.strip() for p in range_string.split(",") if p.strip()]
  ranges = []
  for part in parts:
    a_str, b_str = part.split("-")
    a = int(a_str); b = int(b_str)
    ranges.append((a, b))

  if not ranges:
    return 0

  global_min = min(a for a, _ in ranges)
  global_max = max(b for _, b in ranges)

  invalid_ids = _generate_invalid_ids_in_bounds(global_min, global_max)

  total = 0
  for a, b in ranges:
    # sum only invalid IDs that fall in this range
    total += sum(n for n in invalid_ids if a <= n <= b)

  return total

def sum_invalid_ids_from_file(file_path: str) -> int:
  """
    Reads a single-line range definition from a text file and computes
    the sum of all invalid IDs found in the ranges.

    :param file_path: Path to the input text file.

    :return: The total sum of all invalid IDs across all ranges in the file.
    """
  with open(file_path, "r", encoding="utf-8") as fh:
    range_string = fh.readline().strip()
  return sum_invalid_ids_from_ranges(range_string)

def main():
  '''Program Entry Point'''

  dirname = os.path.dirname(__file__)
  INPUT_FILE = os.path.join(dirname, "input.txt")

  total = sum_invalid_ids_from_file(INPUT_FILE)
  print("Total Invalid ID Sum:", total)

# Program Entry Point
if __name__ == "__main__":
  main()