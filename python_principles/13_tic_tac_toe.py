def get_row_col(string: str) -> tuple:
    return (int(string[1]) - 1, {"A": 0, "B": 1, "C": 2}[string[0]])
    # return ({"1": 0, "2": 1, "3": 2}[choice[1]], {"A": 0, "B": 1, "C": 2}[choice[0]])


if __name__ == "__main__":
    print(get_row_col("C1"))
