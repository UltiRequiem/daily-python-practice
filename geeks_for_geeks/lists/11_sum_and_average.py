NUMBERS = (4, 5, 6)


COUNT = sum(NUMBERS)

AVERAGE = round(COUNT / len(NUMBERS), 2)

if __name__ == "__main__":
    print("Sum of all items in the list:", COUNT)
    print("Average of all items in the list:", AVERAGE)
