MY_LIST = [10, 11, 12, 13, 14, 15]


def reverse_list(lst: list) -> list:
    new_lst = lst.copy()
    new_lst.reverse()
    return new_lst


if __name__ == "__main__":
    print(reverse_list(MY_LIST))
