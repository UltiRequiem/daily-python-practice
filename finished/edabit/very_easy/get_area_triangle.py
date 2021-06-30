def tri_area(base: int, height: int) -> int:
    return round((base * height) / 2)


# tri_area_lambda = lambda b, h: (b * h) / 2

# Test: Take the base and height of a triangle and return its area
if __name__ == "__main__":
    print(tri_area(50, 7))
