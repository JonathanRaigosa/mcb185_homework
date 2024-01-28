# Reporting the Oligo Melting Temperature by Jonathan Raigosa

import math
import sys

def calculate_temp(a, t, g, c): # Calculate the melting temp of an oligo
	total = a + t + g + c
	if total <= 13:
		tm1 = (a + t) * 2 + (g + c) * 4
		return tm1
	if total > 13 and g + c > 16.4:
		tm2 = 64.9 + 41 * (g + c - 16.4) / (total)
		return tm2

#Labeling the values used for a, t, g, c
oligo1 = (7, 4, 3, 1)
oligo2 = (54, 90, 20, 40)
oligo3 = (1, 7, 4, 2)
oligo4 = (3, 9, 5, 6)

#Print the values of each oligo
print(calculate_temp(7, 4, 3, 1), oligo1)
print(calculate_temp(54, 90, 20, 40), oligo2)
print(calculate_temp(1, 7, 4, 2), oligo3)
print(calculate_temp(3, 0, 5, 6), oligo4)