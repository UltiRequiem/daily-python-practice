def count(word: str):
    return word.count("-") + 1
    # return len(word.split("-"))


if __name__ == "__main__":
    print(count("ho-tel"))
