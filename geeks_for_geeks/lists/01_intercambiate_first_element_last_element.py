# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list


NUMBERS = [12, 35, 9, 56, 24]


def swap_list(list_to_swap: list) -> list:

    list_to_swap[0], list_to_swap[-1] = list_to_swap[-1], list_to_swap[0]

    return list_to_swap


print(swap_list(NUMBERS))
