TEST_ONE = ["Gfg", "is", "best"]
TEST_TWO = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]


def main(lst_one: list, lst_two: list):
    return [lst_one[idx] for idx in lst_two]


if __name__ == "__main__":
    print(main(TEST_TWO, TEST_TWO))
