MY_LIST = []

num = int(input("Enter number of elements in list: "))

for number in range(1, num + 1):
    ele = int(input("Enter elements: "))
    MY_LIST.append(ele)

print("The smallest element is:{min(MY_LIST)}")
