NUMBERS = (-10, 21, 4, -45, -66, 93, -11)


def positives(lst: list | tuple)->list:
    return [num for num in lst if num > 0]
    # return list(filter(lambda x: x > 0, lst))


POSITIVE_LIST = positives(NUMBERS)

if __name__ == "__main__":
    print(f"Positive numbers in the list: {POSITIVE_LIST}")
