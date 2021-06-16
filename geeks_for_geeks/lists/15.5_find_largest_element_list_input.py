MY_LIST = []

NUM = int(input("Enter number of elements in list: "))

for number in range(1, NUM + 1):
    ele = int(input("Enter elements: "))
    MY_LIST.append(ele)

print("The Largest element is: {max(MY_LIST)}")
