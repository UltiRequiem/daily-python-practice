EXAMPLE = [
    (),
    ("ram", "15", "8"),
    (),
    ("laxman", "sita"),
    ("krishna", "akbar", "45"),
    ("", ""),
    (),
]


def remove_empty(tuples):
    tuples = [tupla for tupla in tuples if tupla]
    return tuples


print(remove_empty(EXAMPLE))
