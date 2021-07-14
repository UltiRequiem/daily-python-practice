WORDS = ["geekforgeeks", "is", "best", "for", "geeks"]


def find_char(lst: list[str], k: int):
    return [ele[0] for sub in enumerate(lst) for ele in enumerate(sub[1])][k]


if __name__ == "__main__":
    print(f"The original list is : {WORDS}")
    # 15th index occurs in best and point to e which is 1st element of word
    print(f"Index of character at Kth position word : {find_char(WORDS,15)}")
