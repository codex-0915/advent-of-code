#!/usr/bin/env python3

# Advent of Code 2025 Day 1 Part 1 Solution

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


def count_zero_landings(rotations: list[str], start_position: int = 50) -> int:
  """
  Simulates a rotating safe dial (0–99) and counts how many times
  the dial lands on 0 after a rotation.

  The dial wraps around:
  - Left from 0 goes to 99
  - Right from 99 goes to 0

  Args:
    rotations (list[str]): List of rotations like ["L68", "R48", ...]
    start_position (int): Initial dial position (default is 50)

  Returns:
    int: Number of times the dial lands on 0 after any rotation
  """
  position = start_position
  zero_count = 0

  for move in rotations:
    direction = move[0].upper()   # 'L' or 'R'
    distance = int(move[1:])      # number of clicks

    if direction == "L":
      position = (position - distance) % 100
    elif direction == "R":
      position = (position + distance) % 100
    else:
      raise ValueError(f"Invalid rotation: {move}")

    if position == 0:
      zero_count += 1

  return zero_count

def main():
    """
    Main execution entry point for the Safe Dial Rotation Simulator.

    This script reads a sequence of dial rotations from an input text file,
    where each line represents a rotation instruction in the format:
    - 'L<number>' for rotating left
    - 'R<number>' for rotating right

    The dial:
    - Has values from 0 to 99
    - Starts at position 50
    - Wraps around circularly (0 ↔ 99)

    The program simulates all rotations in order and counts how many times
    the dial lands exactly on position 0 after any rotation. This count
    represents the actual password, as the safe itself is a decoy.

    Output:
        Prints the total number of times the dial lands on 0.
    """
    dirname = os.path.dirname(__file__)
    data = os.path.join(dirname, "input.txt")

    rotations = extract_lines(data)
    result = count_zero_landings(rotations)

    print(f"Dial landed on 0 a total of {result} times.")

if __name__ == "__main__":
    main()

