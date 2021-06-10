# https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list
"""
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
"""

original_list = [23, 65, 19, 90]
first_position, second_position = 1, 3


def swapPositions(list, position_one, position_two):

    list[position_one], list[position_two] = list[position_two], list[position_one]
    return list


print(f"The orginal List is: {original_list}.")
swapped_list = swapPositions(original_list, first_position - 1, second_position - 1)
print(f"The swapped list is: {swapped_list}.")
