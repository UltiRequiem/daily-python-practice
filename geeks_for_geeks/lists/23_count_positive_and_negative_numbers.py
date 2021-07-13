NUMBERS = (-10, -21, -4, -45, -66, -93, 11)


def count_positives(lst: list[int] | tuple[int]) -> int:
    return len([num for num in lst if num >= 1])
    # return len(list(filter(lambda x: x >= 0, lst)))


POS_COUNT = count_positives(NUMBERS)

if __name__ == "__main__":
    print(f"Positive numbers in the list: {POS_COUNT}.")
    print(f"Negative numbers in the list: {len(NUMBERS) - POS_COUNT}.")
