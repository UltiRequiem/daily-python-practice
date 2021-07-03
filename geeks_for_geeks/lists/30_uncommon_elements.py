TEST_ONE = [[1, 2], [3, 4], [5, 6]]
TEST_TWO = [[3, 4], [5, 7], [1, 2]]

print(f"The original list 1 : {TEST_ONE}")
print(f"The original list 2 : {TEST_TWO}")

RES = set(map(tuple, TEST_ONE)) ^ set(map(tuple, TEST_TWO))
UNCOMMON = list(map(list, RES))

print(f"The uncommon of two lists is : {UNCOMMON}")
