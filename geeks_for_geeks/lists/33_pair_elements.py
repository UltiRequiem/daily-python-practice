TEST = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]


def main(lst: list) -> list:
    res = []
    for sub in lst:
        res.append([[ele, sub[-1]] for ele in sub[:-1]])
    return res


if __name__ == "__main__":
    print(f"The original list is : {TEST}")
    print(f"The list after pairing is : {main(TEST)}")
