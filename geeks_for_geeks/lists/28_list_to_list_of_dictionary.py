TEST = ("Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33)
KEYS = ("name", "number")


def main(keys: list | tuple, lst: list | tuple) -> list:
    return [{keys[0]: lst[i], keys[1]: lst[i + 1]} for i in range(0, len(lst), 2)]


if __name__ == "__main__":
    print(f"The original list :{TEST} ")
    print(f"The constructed dictionary list :{main(KEYS,TEST)}")
