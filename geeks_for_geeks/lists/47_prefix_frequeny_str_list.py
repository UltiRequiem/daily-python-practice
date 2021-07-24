STRINGS = ["gfgisbest", "geeks", "gfgfreak", "gfgCS", "Gcourses"]


def main(sub: str, lst: list) -> int:
    return sum(s.startswith(sub) for s in lst)


if __name__ == "__main__":
    print(f"The original list is: {STRINGS}")
    print(f"Strings count with matching frequency: {main('gfg',STRINGS)}")
