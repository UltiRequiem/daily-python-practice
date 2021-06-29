MY_LIST = []

NUM = int(input("Enter number of elements in list: "))

for number in range(1, NUM + 1):
    ele = int(input("Enter elements: "))
    MY_LIST.append(ele)

if __name__ == "__main__":
    print("The smallest element is:{min(MY_LIST)}")
