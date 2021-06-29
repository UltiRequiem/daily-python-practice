# https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list
"""
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
"""

ORIGINAL_LIST = [23, 65, 19, 90]
FIRST_POSITION, SECOND_POSITION = 1, 3


def swap_positions(a_list: list, pos_one: int, pos_two: int) -> list:

    a_list[pos_one], a_list[pos_two] = (
        a_list[pos_two],
        a_list[pos_one],
    )
    return a_list


SWAPPED_LIST = swap_positions(ORIGINAL_LIST, FIRST_POSITION - 1, SECOND_POSITION - 1)

print(f"The orginal List is: {ORIGINAL_LIST}.")
print(f"The swapped list is: {SWAPPED_LIST}.")
