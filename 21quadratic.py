# Quadratic Formula by Jonathan Raigosa

import math

def quadratic_formula(a, b, c):    # Solves and return to X-intercepts
	change = math.sqrt(b**2 - 4 * a * c)


    # Calculate the two X-inercepts
	x1 = (-b + change) / (2 * a)
	x2 = (-b - change) / (2 * a)
    
	return x1, x2

# Example provided
"""
a = 1
b = 4
c = -21

xs = quadratic_formula(a, b, c)
print('Quadratic Formula Roots', xs)
"""

print(quadratic_formula(6, -17, 12))
print(quadratic_formula(1, 5, 6))
print(quadratic_formula(1, 3, -4))
