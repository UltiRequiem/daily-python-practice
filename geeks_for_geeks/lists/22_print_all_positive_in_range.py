START, END = -4, 19


def print_positives_in_range(start: int, end: int) -> None:
    for num in range(start, end):
        if num > 0:
            print(num)


if __name__ == "__main__":
    print_positives_in_range(START, END)
