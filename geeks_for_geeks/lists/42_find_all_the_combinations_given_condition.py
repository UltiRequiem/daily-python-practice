TEST = ["geekforgeeks", [5, 4, 3, 4], "is", ["best", "good", "better", "average"]]


def main(k, lst):
    return [
        [idx if not isinstance(idx, list) else idx[i] for idx in lst]
        for i in range(k - 1)
    ]


if __name__ == "__main__":
    print(f"The original list is : {TEST}")
    print(f"All index Combinations : {main(4,TEST)}")
