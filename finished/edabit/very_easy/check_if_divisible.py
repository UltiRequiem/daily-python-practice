# Return True if an integer is evenly divisible by 5, and False otherwise


def divisible_by_five(number: int) -> bool:
    return number % 5 == 0


# divisible_by_five_lambda = lambda x : x % 5 == 0

if __name__ == "__main__":
    print(divisible_by_five(4456))
