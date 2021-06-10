# https://www.geeksforgeeks.org/python-cloning-copying-list


def clone_list(li1):
    return li1[:]


def main():
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = clone_list(li1)

    # Memory address in hex format
    print("Original List:", hex(id(li1)))
    print("After Cloning:", hex(id(li2)))


if __name__ == "__main__":
    main()
