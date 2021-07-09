NUM = int(input("Enter number of elements in list: "))
NUMBERS = [int(input("Enter elements:")) for _ in range(NUM)]

if __name__ == "__main__":
    print(f"The smallest element is:{min(NUMBERS)}")
