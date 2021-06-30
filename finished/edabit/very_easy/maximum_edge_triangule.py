def next_edge(side_one: int, side_two: int) -> int:
    return (side_one + side_two) - 1


# next_edge_lambda = lambda s_1, s_2: (s_1 + s_2) - 1

# Test: Finds the maximum range of a triangle's third edge,
# where the side lengths are all integers
if __name__ == "__main__":
    print(next_edge(24, 58))
