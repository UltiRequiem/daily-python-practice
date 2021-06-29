# https://www.geeksforgeeks.org/python-cloning-copying-list

NUMBERS = [4, 8, 2, 10, 15, 18]


def clone_list(li1: list) -> list:
    return li1[:]


def main(list_to_clone):
    # Memory address in hex format
    print("Original List:", hex(id(list_to_clone)))
    print("After Cloning:", hex(id(clone_list(list_to_clone))))


if __name__ == "__main__":
    main(NUMBERS)
