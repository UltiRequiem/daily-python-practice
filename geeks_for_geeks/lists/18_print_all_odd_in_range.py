def print_odd_in_range(start: int, end: int)->None:
    for num in range(start, end + 1):
        if num % 2:
            print(num)


if __name__ == "__main__":
    print_odd_in_range(3, 55)
