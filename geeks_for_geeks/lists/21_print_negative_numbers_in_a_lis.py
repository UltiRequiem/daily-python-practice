NUMBERS = ( -10, 21, 4, -45, -66, 93, -11 )

NEGATIVE_LIST = list(filter(lambda x: x < 0, NUMBERS))

if __name__ == "__main__":
    print(f"Positive numbers in the list: {NEGATIVE_LIST}")
