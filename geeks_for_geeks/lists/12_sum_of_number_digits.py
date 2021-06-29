NUMBERS = (12, 67, 98, 34)

print("The original list is : " + str(NUMBERS))

RESULT = list(map(lambda i: sum(int(char) for char in str(i)), NUMBERS))

if __name__ == "__main__":
    print("List Integer Summation : " + str(RESULT))
