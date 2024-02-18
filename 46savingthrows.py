# Saving Throws by Jonathan Raigosa; Help from class Jordan Shore.

import random

def roll_norm():
	return random.randint(1, 20)

def roll_disadvant():
	ro1 = random.randint(1, 20)
	ro2 = random.randint(1, 20)
	if ro1 <= ro2:
		return ro1
	else:
		return ro2

def roll_advant():
	ro1 = random.randint(1, 20)
	ro2 = random.randint(1, 20)
	if ro1 >= ro2:
		return ro1
	else:
		return ro2

trials = 10000
print('DC\tnorm\tadv\tdis')
for dc in range(5, 16, 5):
	print(f'{dc}\t', end='')
	success_norm = 0
	success_advant = 0
	success_disadvant = 0
	for i in range(trials):
		rn = roll_norm()
		ra = roll_advant()
		rd = roll_disadvant()
		if rn >= dc:
			success_norm += 1
		if ra >= dc:
			success_advant += 1
		if rd >= dc:
			success_disadvant += 1

	print(f'{success_norm / trials}\t', end='')
	print(f'{success_advant / trials}\t', end='')
	print(f'{success_disadvant / trials}\t')
	