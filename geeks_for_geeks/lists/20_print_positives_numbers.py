number_list = [-10, 21, 4, -45, -66, 93, -11]

if __name__ == "__main__":
    print(
        f"Positive numbers in the list: {list(filter(lambda x: x > 0, number_list))}"
        )
