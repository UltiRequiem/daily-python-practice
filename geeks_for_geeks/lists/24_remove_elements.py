NUMBERS = [1, 2, 3]


def del_elements(ele: int, lst: list) -> list:
    """Remove an element from a list"""
    new_lst = lst.copy()
    new_lst.remove(ele)
    return new_lst


TEST = del_elements(3, NUMBERS)

if __name__ == "__main__":
    print(f"Original list: {NUMBERS}.")
    print(f"Now: {TEST}")
