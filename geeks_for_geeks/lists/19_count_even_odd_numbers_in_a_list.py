MY_LIST = ( 10, 21, 4, 45, 66, 93, 11 )

ONLY_ODD = len([num for num in MY_LIST if num % 2 == 1])
ONLY_EVEN = len(MY_LIST) - ONLY_ODD

if __name__ == "__main__":
    print(f"Even numbers in the list: {ONLY_EVEN}.")
    print(f"Odd numbers in the list: {ONLY_ODD}.")
