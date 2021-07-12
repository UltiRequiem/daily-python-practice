TEXT = ("geeks", "for", "geeks", "is", "best")


def revert_strings(lst: list | tuple):
    return [string[::-1] for string in lst]


if __name__ == "__main__":
    print(f"The original list is: {TEXT}")
    print(f"The reversed string list is: {revert_strings(TEXT)}")
