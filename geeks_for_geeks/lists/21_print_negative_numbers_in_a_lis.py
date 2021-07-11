NUMBERS = (-10, 21, 4, -45, -66, 93, -11)


def negatives(lst: list | tuple):
    return [num for num in lst if num < 0]
    # return list(filter(lambda x: x < 0, lst))

NEGATIVE_LIST = negatives(NUMBERS)

if __name__ == "__main__":
    print(f"Positive numbers in the list: {NEGATIVE_LIST}")
