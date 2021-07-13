"""
Given a list of lists. The task is to extract a random element from it.
"""
from random import choice


TEST = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]


def flatten(t: list[list[int]] | tuple) -> int:
    return choice([item for sublist in t for item in sublist])


if __name__ == "__main__":
    print(TEST)
    print(flatten(TEST))
