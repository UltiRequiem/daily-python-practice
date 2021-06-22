# Return the largest number in the list

NUMBERS = [1000, 1001, 857, 1]


def find_largest_num(nums):
    return max(nums)


# find_largest_num_lambda = lambda n: max(n)

if __name__ == "__main__":
    print(find_largest_num(NUMBERS))
