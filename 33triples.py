# Triples by Jonathan Raigosa

import math

def perfect_square(n): 
	if math.isclose(math.sqrt(n), math.sqrt(n) // 1): 
		return True
	return False
# Checks to see if perfect square

def triples(n):
	for i in range(1, n):
		for y in range(i + 1, n):
# Nested Loops
			if perfect_square(i**2 + y**2) and i < y:
				print(i, y, int(math.sqrt(i**2 + y**2)))
# Calculates the square root of c...
				
triples(100)