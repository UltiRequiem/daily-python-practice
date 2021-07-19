from itertools import product

LETTERS = ["b", "c", "d"]
NUMS = [1, 4, 9]


def unique_combination(lst_one: list, lst_two: list):
    return [list(zip(lst_one, i)) for i in product(lst_two, repeat=len(lst_one))]


if __name__ == "__main__":
    print(unique_combination(LETTERS, NUMS))
