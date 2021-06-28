TEST = [5, 6, [], 3, [], [], 9]

print(f"The original list is : {TEST}")


res = [ele for ele in TEST if ele != []]
# res = list(filter(None, TEST))

print(f"List after empty list removal :{res} ")
