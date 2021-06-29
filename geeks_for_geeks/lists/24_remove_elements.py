NUMBERS = [1, 2, 3]


def del_elements(ele: int, lst: list) -> list:
    return lst.remove(ele)


if __name__ == "__main__":
    print(f"Original list: {NUMBERS}.")
    del_elements(2, NUMBERS)
    print(f"Now: {NUMBERS}")
