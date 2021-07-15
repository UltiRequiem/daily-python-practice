NUMBERS = [4, 5, 6, 7, 3, 9]


def contain_ele_in_range(i: int, j: int, lst: list) -> bool:
    return all(ele >= i and ele < j for ele in lst)


res = contain_ele_in_range(3, 10, NUMBERS)

if __name__ == "__main__":
    print(f"The original list is: {NUMBERS}")
    print(f"Does list contain all elements in range: {res}")
