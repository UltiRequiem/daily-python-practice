def mid(word: str | list | tuple) -> str:
    if len(word) % 2 == 0:
        return ""
    # return word[math.floor(len(word) / 2)]
    return word[round(len(word) // 2)]


if __name__ == "__main__":
    print(mid("hello"))  # "l"
    print(mid("12345"))  # "3"
    print(mid("hello2"))  # ""
    print(mid("abc"))  # "b"
    # It also works with lists!
    print(mid(["a", "b", "c", "d", "e"]))  # "c"
    print(mid(("1", "2", "3", "4", "5")))  # "3"
