NUMBERS = (10, 21, 4, 45, 66, 93, 11)


def count_odd(lst: list[int] | tuple[int]) -> int:
    return len([num for num in lst if num % 2 == 1])


ONLY_ODD = count_odd(NUMBERS)
ONLY_EVEN = len(NUMBERS) - ONLY_ODD


if __name__ == "__main__":
    print(f"Even numbers in the list: {ONLY_EVEN}.")
    print(f"Odd numbers in the list: {ONLY_ODD}.")
