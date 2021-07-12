from functools import reduce

TEST = [0, 3, 5, 6, 3, 5, 6, 1]
# The set method clear the repeated elements
FILTRED = set(TEST)


def prod(lst: list | set) -> int:
    return reduce(lambda acum, ele: acum * ele, lst)


if __name__ == "__main__":
    print(f"The original list is : {TEST}")
    print(f"Duplication removal list product {prod(FILTRED)}.")
