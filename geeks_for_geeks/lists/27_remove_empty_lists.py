TEST = [5, 6, [], 3, [], [], 9]


# res = list(filter(None, TEST))
def clear_empty(lst: list) -> list:
    return [ele for ele in TEST if ele]
    # return list(filter(lambda ele: ele, lst))


if __name__ == "__main__":
    print(f"The original list is : {TEST}")
    print(f"List after empty list removal :{clear_empty(TEST)} ")
