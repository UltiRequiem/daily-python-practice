# Return the difference between the biggest and smallest numbers

NUMBERS = (10, 4, 1, 4, 32, 21)


def difference_max_min(numbers_list: tuple or list) -> int:
    return max(numbers_list) - min(numbers_list)


# difference_max_min_lambda = lambda l: max(l) - min(l)

if __name__ == "__main__":
    print(difference_max_min(NUMBERS))
