def count_ocurrences(dictionary: dict, word: str | int) -> int:
    return sum(value == word for value in dictionary.values())
    # return len([p for p in statuses if statuses[p] == word])


STATUSES = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Eve Two": "online",
}

if __name__ == "__main__":
    print(count_ocurrences(STATUSES, "online"))