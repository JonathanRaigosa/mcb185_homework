# dnd stats by Jonathan Raigosa, Amima Muhic class example

import random

rolls = 10000
three_times = 3

# dnd 3D6, rolling 3 six-sided dice

total_3d6 = 0

for i in range(rolls):
	score = 0
	for j in range(three_times):
		d6 = random.randint(1, 6)
		# line produces a random number for a dice
		score += d6
	total_3d6 += score
print(f'3D6\t{total_3d6 / rolls}')
# Should yield 10.5 roughly

# 3D6r1, rolling 3 six-sided dice, re-roll 1s
total_3d6r1 = 0

for i in range(rolls):
	score = 0
	for j in range(three_times):
		d6 = random.randint(1, 6)
		if d6 == 1: d6 = random.randint(1, 6)
# this line is forcing a another roll when roll is 1
		score += d6
	total_3d6r1 += score
print(f'3D6r1\t{total_3d6r1 / rolls}')

# 3D6r2, rolling 2 six sided dice 3 times, take max
total_3d6r2 = 0

for i in range(rolls):
	score = 0
	for j in range(three_times):
		d6_1 = random.randint(1, 6)
		d6_2 = random.randint(1, 6)
		if d6_2 >= d6_1:
			score += d6_2
		else:
			score += d6_1
	total_3d6r2 += score
print(f'3D6r2\t{total_3d6r2 / rolls}')

# 4D6d1, rolling 4 six sided dice, dropping lowest
total_4dr1 = 0

for i in range(rolls):
	score = 0
	d6_1 = random.randint(1, 6)
	d6_2 = random.randint(1, 6)
	d6_3 = random.randint(1, 6)
	d6_4 = random.randint(1, 6)
	
	mini_roll = d6_1
	if d6_2 < mini_roll:
		mini_roll = d6_2
	if d6_3 < mini_roll:
		mini_roll = d6_3
	if d6_4 < mini_roll:
		mini_roll = d6_4

# lowest roll identified and subtracted

	score = d6_1 + d6_2	+ d6_3 + d6_4 - mini_roll
	
	total_4dr1 += score

print(f'4Dr1\t{total_4dr1 / rolls}')