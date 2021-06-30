# Returns the last item in the list

WORDS = ("cat", "dog", "duck")


def get_last_item(lst: tuple or list):
    return lst[-1]


# get_last_item_lambda = lambda l: l[-1]

if __name__ == "__main__":
    print(get_last_item(WORDS))
