def list_xor(val, lst_one: list, lst_two: list) -> bool:
    return (val in lst_one) ^ (val in lst_two)


if __name__ == "__main__":
    print(list_xor(1, [1, 2, 3], [4, 5, 6]))
    print(list_xor(1, [0, 2, 3], [1, 5, 6]))
    print(list_xor(1, [1, 2, 3], [1, 5, 6]))
    print(list_xor(1, [0, 0, 0], [4, 5, 6]))
