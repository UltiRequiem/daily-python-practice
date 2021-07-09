NUMBERS = (-10, 21, 4, -45, -66, 93, -11)

# POSITIVE_LIST = list(filter(lambda x: x > 0, NUMBERS))
POSITIVE_LIST = [num for num in NUMBERS if num > 0]

if __name__ == "__main__":
    print(f"Positive numbers in the list: {POSITIVE_LIST}")
