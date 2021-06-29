# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list


NUMBERS = [12, 35, 9, 56, 24]


def swap_last_element(list_to_swap: list) -> list:
    """Intercambiate first element with the last in the list"""

    list_to_swap[0], list_to_swap[-1] = list_to_swap[-1], list_to_swap[0]

    return list_to_swap


if __name__ == "__main__":
    print(swap_last_element(NUMBERS))
