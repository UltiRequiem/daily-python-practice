# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list


my_list = [12, 35, 9, 56, 24]


def swapList(list_to_swap):

    list_to_swap[0], list_to_swap[-1] = list_to_swap[-1], list_to_swap[0]

    return list_to_swap


print(swapList(my_list))
