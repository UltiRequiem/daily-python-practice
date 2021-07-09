NUMBERS = (12, 67, 98, 34)

print(f"The original list is : {NUMBERS}")


def sum_digits(array: list | tuple) -> int:
    return sum(list(map(lambda i: sum(int(char) for char in str(i)), array)))


if __name__ == "__main__":
    print(f"List Integer Summation : {sum_digits(NUMBERS)}")
