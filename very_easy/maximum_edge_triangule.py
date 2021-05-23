def next_edge(side1, side2):
	return (side1 + side2) - 1 

# Test: Finds the maximum range of a triangle's third edge, 
# where the side lengths are all integers
print(next_edge(24,58))
