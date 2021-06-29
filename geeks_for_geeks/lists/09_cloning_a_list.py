# https://www.geeksforgeeks.org/python-cloning-copying-list

NUMBERS = [4, 8, 2, 10, 15, 18]


def clone_list(lst: list) -> list:
    """Clone a List"""
    return lst[:]


def main(list_to_clone: list) -> None:
    """Print the memory address in hex Format"""
    print("Original List:", hex(id(list_to_clone)))
    print("After Cloning:", hex(id(clone_list(list_to_clone))))


if __name__ == "__main__":
    main(NUMBERS)
