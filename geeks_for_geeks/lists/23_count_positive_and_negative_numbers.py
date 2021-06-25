MY_LIST = (-10, -21, -4, -45, -66, -93, 11)

POS_COUNT = len([num for num in MY_LIST if num >= 1])

if __name__ == "__main__":
    print(f"Positive numbers in the list: {POS_COUNT}.")
    print(f"Negative numbers in the list: {len(MY_LIST) - POS_COUNT}.")
