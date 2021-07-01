NUMBERS = (4, 5, 6)


COUNT = sum(NUMBERS)

AVERAGE = round(COUNT / len(NUMBERS))

if __name__ == "__main__":
    print(f"The sum of all items in the list is {COUNT}.")
    print(f"The average of all items in the list is {AVERAGE}.")
