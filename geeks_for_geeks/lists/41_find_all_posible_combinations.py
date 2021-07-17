from itertools import permutations


def find_combinations(lst: list):
    return permutations(lst, len(lst))

if __name__ == "__main__":
    for i in find_combinations([1,2,3,4]):
        print(i)
