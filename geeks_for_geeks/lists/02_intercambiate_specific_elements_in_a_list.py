# https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list
"""
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
"""

NUMBERS = [23, 65, 19, 90]


def swap_positions(lst: list, pos_one: int, pos_two: int) -> list:
    """Intercambiate specific elements in a list"""
    new_lst = lst.copy()

    new_lst[pos_one], new_lst[pos_two] = lst[pos_two], lst[pos_one]

    return new_lst


SWAPPED_LIST = swap_positions(NUMBERS, 1, 3)

if __name__ == "__main__":
    print(f"The orginal List is: {NUMBERS}.")
    print(f"The swapped list is: {SWAPPED_LIST}.")
