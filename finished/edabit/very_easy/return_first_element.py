# Create a function that takes a list containing only numbers and return the first element
NUMBERS = [1, 2, 3]


def get_first_value(number_list):
    return number_list[0]


get_first_value_lambda = lambda number_list: number_list[0]

if __name__ == "__main__":
    print(get_first_value(NUMBERS))
