# Monte Carlo pi estimate by Jonathan Raigosa.

import random

point_total = 0
points_in_circle = 0

while True:
	x = random.random()
	y = random.random()
# x and y value between 0 and 1 randomly generated
	
	origin_length = x**2 + y**2
	
	if origin_length <= 1:
		points_in_circle += 1
# finds all the points in the circle
	point_total += 1
# takes all the points in total
	
	mc_pi_estimate = (points_in_circle / point_total) * 4
	
	print(f'Trials {point_total}: Monte Carlo Pi estimate = {mc_pi_estimate}')