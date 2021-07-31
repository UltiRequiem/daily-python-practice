def flatten(lst_of_lst: list) -> list:
    return [item for sublist in lst_of_lst for item in sublist]


if __name__ == "__main__":
    print(flatten([[1, 2], [3, 4], [5, 6]]))
