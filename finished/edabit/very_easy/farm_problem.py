# Implement a function that returns the total number of legs of all the animals


def animals(chickens, cows, pigs):
    return (chickens * 2) + (cows * 4) + (pigs * 4)


# animals_lambda = lambda chi, co, p: (chi * 2) + (co * 4) + (p * 4)

if __name__ == "__main__":
    print(animals(2, 3, 5))
