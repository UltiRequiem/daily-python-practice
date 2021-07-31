def is_anagram(one: str, two: str):
    return sorted(one) == sorted(two)


if __name__ == "__main__":
    print(is_anagram("typhoon", "opython"))
    print(is_anagram("Alice", "Bob"))
