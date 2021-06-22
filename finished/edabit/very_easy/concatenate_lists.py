# Concatenate two integer lists

LIST_ONE = [7, 8]
LIST_TWO = [10, 9, 1, 1, 2]


def concat(fir_list, second_list):
    return fir_list + second_list


# concat_lambda = lambda x, y: x + y

if __name__ == "__main__":
    print(concat(LIST_ONE, LIST_TWO))
