# Create a function that takes a number num and returns its length


def number_lenght(num: int) -> int:
    return len(str(num))


# number_lenght_lambda = lambda x: len(str(x))

if __name__ == "__main__":
    print(number_lenght(25000))
