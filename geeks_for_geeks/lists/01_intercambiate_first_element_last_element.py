# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list


NUMBERS = [12, 35, 9, 56, 24]


def swap_last_element(lst_to_swap: list) -> list:
    """Intercambiate first element with the last in the list"""
    new_lst = lst_to_swap.copy()

    new_lst[0], new_lst[-1] = lst_to_swap[-1], lst_to_swap[0]

    return new_lst


if __name__ == "__main__":
    print(swap_last_element(NUMBERS))
