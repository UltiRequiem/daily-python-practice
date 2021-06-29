NUMBERS = (-10, -21, -4, -45, -66, -93, 11)

POS_COUNT = len([num for num in NUMBERS if num >= 1])

if __name__ == "__main__":
    print(f"Positive numbers in the list: {POS_COUNT}.")
    print(f"Negative numbers in the list: {len(NUMBERS) - POS_COUNT}.")
