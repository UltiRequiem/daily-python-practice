def palindrome(string: str) -> bool:
    return string == string[::-1]


if __name__ == "__main__":
    print(palindrome("bob"))
    print(palindrome("ana"))
    print(palindrome("pedro"))
