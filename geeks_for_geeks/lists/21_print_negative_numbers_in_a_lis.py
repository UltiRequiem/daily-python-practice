NUMBER_LIST = [-10, 21, 4, -45, -66, 93, -11]

NEGATIVE_LIST = list(filter(lambda x: x < 0, NUMBER_LIST))

if __name__ == "__main__":
    print(f"Positive numbers in the list: {NEGATIVE_LIST}")