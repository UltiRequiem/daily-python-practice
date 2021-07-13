TEST = ([4, 1, 6], [7, 8], [4, 10, 8])


def row_sort(lst: list[list[int]] | tuple) -> list[list[int]]:
    return [sorted(sub, reverse=True) for sub in lst]


if __name__ == "__main__":
    print(f"The original list is : {TEST}")
    print(f"The reverse sorted Matrix is : {row_sort(TEST)}")
