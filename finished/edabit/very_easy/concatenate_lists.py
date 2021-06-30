# Concatenate two integer lists

LIST_ONE = (7, 8)
LIST_TWO = (10, 9, 1, 1, 2)


def concat(first_lst: tuple, second_lst: tuple) -> tuple:
    return first_lst + second_lst


# concat_lambda = lambda x, y: x + y

if __name__ == "__main__":
    print(concat(LIST_ONE, LIST_TWO))
