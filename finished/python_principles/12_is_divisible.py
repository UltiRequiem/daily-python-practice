def if_divisible(num, div=3):
    return num % div == 0


if __name__ == "__main__":
    print(if_divisible(3))
    print(if_divisible(50, 50))
