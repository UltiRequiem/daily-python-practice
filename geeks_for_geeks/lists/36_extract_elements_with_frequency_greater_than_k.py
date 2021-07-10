"""
Given a List, extract all elements whose frequency is greater than K.
"""

TEST = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]


def extract(lst: list, k: int) -> set:
    return set([i for i in lst if lst.count(i) > k])


if __name__ == "__main__":
    print(f"The original list : {TEST}")
    print(f"The required elements : {extract(TEST, 2)}")
