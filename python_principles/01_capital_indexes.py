def capital_indexes(indexes: str) -> list:
    return [letter for letter, char in enumerate(indexes) if char.isupper()]
    # return [letter for letter in range(len(indexes)) if indexes[letter].isupper()]


if __name__ == "__main__":
    print(capital_indexes("mYtESt"))  # [1, 3, 4]
