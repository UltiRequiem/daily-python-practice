from functools import reduce

MY_LIST = (4, 2, 3, 29, 89)

print(reduce((lambda x, y: x * y), MY_LIST))
