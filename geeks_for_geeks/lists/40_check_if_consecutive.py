NUMS = [4, 5, 5, 5, 3, 8]


def check_consecutive(lst: list, conse: int):
    for i in range(len(lst) - 2):
        if lst[i] == lst[i + 1] and lst[i + 1] == lst[i + 2]:
            print(lst[i])


check_consecutive(NUMS, 3)
