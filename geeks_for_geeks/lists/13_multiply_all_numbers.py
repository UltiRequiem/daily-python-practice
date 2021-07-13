from functools import reduce

NUMBERS = (4, 2, 3, 29, 89)


def multiply_all(lst: list[int] | tuple[int]) -> int:
    return reduce(lambda acum, curr: acum * curr, lst)


if __name__ == "__main__":
    print(multiply_all(NUMBERS))
