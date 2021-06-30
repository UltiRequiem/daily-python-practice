# Return the total sum of internal angles (in degrees)
def sum_polygon(n: int) -> int:
    return (n - 2) * 180


# sum_polygon_lambda = lambda n: (n - 2) * 180

if __name__ == "__main__":
    print(sum_polygon(24))
