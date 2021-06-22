# Lambda function with if but without else.

square = lambda x: x * x if (x > 0) else None

if __name__ == "__main__":
    print(square(3))
