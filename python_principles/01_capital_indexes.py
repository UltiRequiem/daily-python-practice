def capital_indexes(string: str) -> list:
    return [index for index, char in enumerate(string) if char.isupper()]
    # return [letter for letter in range(len(indexes)) if indexes[letter].isupper()]


if __name__ == "__main__":
    print(capital_indexes("mYtESt"))  # [1, 3, 4]
