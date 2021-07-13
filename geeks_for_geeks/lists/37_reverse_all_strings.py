TEXT = ("geeks", "for", "geeks", "is", "best")


def revert_strings(lst: list[str] | tuple[str]) -> list[str]:
    return [string[::-1] for string in lst]
    # return list(map(lambda i: i[::-1], lst))


if __name__ == "__main__":
    print(f"The original list is: {TEXT}")
    print(f"The reversed string list is: {revert_strings(TEXT)}")
