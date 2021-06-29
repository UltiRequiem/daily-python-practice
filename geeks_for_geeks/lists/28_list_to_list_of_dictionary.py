TEST = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
KEYS = ["name", "number"]


def main(keys, a_list):
    return [
        {keys[0]: a_list[i], keys[1]: a_list[i + 1]} for i in range(0, len(a_list), 2)
    ]


if __name__ == "__main__":
    print(f"The original list :{TEST} ")
    res = main(KEYS, TEST)
    print(f"The constructed dictionary list :{res}")
