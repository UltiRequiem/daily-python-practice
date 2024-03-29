# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz", and more specifications...


def fizz_buzz(num: int) -> str:
    # return {True: "Fizz", False: "Buzz"}[num % 3 == 0]
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


if __name__ == "__main__":
    print(fizz_buzz(12))
