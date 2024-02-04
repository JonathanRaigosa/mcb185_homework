# Shannon Entropy Code by Jonathan Raigosa

import math

def shannon_entropy(a, t, g, c):
	total = a + t + g + c


	if total == 0:
		return 0 # If there are not nt, then entropy is zero

# Calculation of probabilities

	prob_a = a / total if a > 0 else 0
	prob_t = t / total if t > 0 else 0
	prob_g = g / total if g > 0 else 0
	prob_c = c / total if c > 0 else 0

# Calculating Entropy using Shannon's Entropy

	entropy = -(prob_a * math.log2(prob_a)) if prob_a > 0 else 0
	entropy += -(prob_t * math.log2(prob_t)) if prob_t > 0 else 0
	entropy += -(prob_g * math.log2(prob_g)) if prob_g > 0 else 0
	entropy += -(prob_c * math.log2(prob_c)) if prob_c > 0 else 0


	return entropy

# Examples
print(shannon_entropy(40, 30, 25, 20))
print(shannon_entropy(10, 50, 7, 0)) 
print(shannon_entropy(0, 0, 0, 0))

