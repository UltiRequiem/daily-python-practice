def next_edge(side1, side2):
    return (side1 + side2) - 1


# next_edge_lambda = lambda s_1, s_2: (s_1 + s_2) - 1

# Test: Finds the maximum range of a triangle's third edge,
# where the side lengths are all integers
if __name__ == "__main__":
    print(next_edge(24, 58))
