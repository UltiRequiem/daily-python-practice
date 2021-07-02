TEST = [["a", "b", 1, 2], ["c", "d", 3, 4], ["e", "f", 5, 6]]


def dict_list(lst: list):
    return {tuple(sub[:2]): tuple(sub[2:]) for sub in lst}


if __name__ == "__main__":
    print(f"The original list is : {TEST}")
    print(f"The mapped Dictionary : {dict_list(TEST)}")
