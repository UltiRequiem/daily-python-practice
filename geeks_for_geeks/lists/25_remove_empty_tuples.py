EXAMPLE = [
    (),
    ("ram", "15", "8"),
    (),
    ("laxman", "sita"),
    ("krishna", "akbar", "45"),
    ("", ""),
    (),
]


def remove_empty(tuples: list) -> list:
    """Remove empty objects"""
    # return [tupla for tupla in tuples if tupla]
    return list(filter(lambda x: x, tuples))


if __name__ == "__main__":
    print(remove_empty(EXAMPLE))
