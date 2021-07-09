START = int(input("Enter the start of range: "))
END = int(input("Enter the end of range: "))

for num in range(START, END):
    print(num if num % 2 == 0 else "", end=" ")
