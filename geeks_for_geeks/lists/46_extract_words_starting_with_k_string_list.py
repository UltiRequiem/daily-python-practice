STRINGS = ["Gfg is best", "Gfg is for geeks", "I love G4G"]


def main(lst: list, k: str) -> list:
    return [ele for temp in lst for ele in temp.split() if ele[0].lower() == k.lower()]


if __name__ == "__main__":
    print(f"The original list is : {STRINGS}")
    print(f"The filtered elements : {main(STRINGS,'g')}")
