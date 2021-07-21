TEST = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]


K = 6

res = [
    idx
    for idx in TEST
    if not any(idx[j] == K and idx[j + 1] == K for j in range(len(idx) - 1))
]

if __name__ == "__main__":
    print("The original list is : " + str(TEST))
    print("The records after removal : " + str(res))
