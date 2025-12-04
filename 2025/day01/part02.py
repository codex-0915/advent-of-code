#!/usr/bin/env python3

# Advent of Code 2025 Day 1 Part 2 Solution

import os

def extract_lines(file_path: str) -> list[str]:
  """
  Reads a text file and extracts each line as a clean string.

  This function opens the specified text file, reads all lines,
  removes leading/trailing whitespace (including newline characters),
  and returns the result as a list of strings.

  Args:
    file_path (str): Path to the input .txt file.

  Returns:
    list[str]: A list containing each line of the file as a cleaned string.
  """
  with open(file_path, "r", encoding="utf-8") as file:
    return [line.strip() for line in file]


def count_zero_clicks(rotations: list[str], start_position: int = 50) -> int:
  """
  Counts the number of times the dial points at 0 during any click,
  including intermediate positions within a rotation.

  Args:
    rotations (list[str]): List of rotations like ["L68", "R48", ...]
    start_position (int): Initial dial position (default 50)

  Returns:
    int: Number of times the dial points at 0 during all rotations
  """
  position = start_position
  zero_count = 0

  for move in rotations:
    direction = move[0].upper()
    distance = int(move[1:])

    step = 1 if direction == "R" else -1

    for _ in range(distance):
      position = (position + step) % 100
      if position == 0:
        zero_count += 1

  return zero_count


def main():
  """
  Main entry point for the Safe Dial Simulator (Method 0x434C49434B).

  Reads rotation instructions from "input.txt" and counts the number
  of times the dial passes through 0 on any click, including during rotations.

  Output:
    Prints the total number of times the dial points at 0.
  """
  dirname = os.path.dirname(__file__)
  data = os.path.join(dirname, "input.txt")
  
  rotations = extract_lines(data)
  result = count_zero_clicks(rotations)

  print(f"Dial pointed at 0 a total of {result} times.")

if __name__ == "__main__":
    main()

