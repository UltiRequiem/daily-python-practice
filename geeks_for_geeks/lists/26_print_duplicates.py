NUMBERS = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]


def repeated(arr: list) -> list:
    array_size = len(arr)
    repeated = []

    for item in range(array_size):
        for number in range(item + 1, array_size):
            if arr[item] == arr[number] and arr[item] not in repeated:
                repeated.append(arr[item])

    return repeated


if __name__ == "__main__":
    print(repeated(NUMBERS))
