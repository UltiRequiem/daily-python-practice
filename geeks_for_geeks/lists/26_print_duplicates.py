NUMBERS = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]


def repeated(array):
    array_size = len(array)
    repeated = []

    for item in range(array_size):
        for number in range(item + 1, array_size):
            if array[item] == array[number] and array[item] not in repeated:
                repeated.append(array[item])

    return repeated


print(repeated(NUMBERS))
