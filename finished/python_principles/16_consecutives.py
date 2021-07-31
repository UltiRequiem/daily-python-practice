def consecutive(string: str, separetor: str = "1") -> int:
    return max([len(c) for c in string.split(separetor)])


if __name__ == "__main__":
    print(consecutive("1001101000110"))
