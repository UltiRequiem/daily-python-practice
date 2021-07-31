"""
Your function return a tuple containing two numbers;
the first should be one lower than the parameter,
and the second should be one higher.
"""


def up_down(num: int) -> tuple:
    return (num - 1, num + 1)


if __name__ == "__main__":
    print(up_down(5))
    print(up_down(3))
