"""
Define a function named all_equal that takes a list and checks
whether all elements in the list are the same.
"""


def all_equal(lst):
    # return all(one == two for one in lst for two in lst)
    return len(set(lst)) <= 1


if __name__ == "__main__":
    print(all_equal([1, 1, 1, 1]))
    print(all_equal([1, 1, 1, 3]))
