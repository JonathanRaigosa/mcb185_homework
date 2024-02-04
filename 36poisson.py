# Poisson probability by Jonathan Raigosa

import math

def poisson(n, k):
	probability = (n ** k * math.e ** (-n) / math.factorial(k))
	return probability

print(poisson(1, 5))
print(poisson(4, 7))
print(poisson(5, 9))