from functools import reduce

NUMBERS = (4, 2, 3, 29, 89)

if __name__ == "__main__":
    print(reduce((lambda x, y: x * y), NUMBERS))
