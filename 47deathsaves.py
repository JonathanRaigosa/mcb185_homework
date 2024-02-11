# Death Saves by Jonathan Raigosa

import random

trials = 10000
die_numb = 0
stable_numb = 0
revived_numb = 0

def dice_roll():
	return random.randint(1, 20)
	
def death_saves():
	success = 0
	failure = 0

	for i in range(trials):
		roll = dice_roll()
	
		if roll == 20:
			return 'revived'
		elif roll >= 10:
			success += 1
		elif roll == 1:
			failure += 2
		else:
			failure += 1

		if success >= 3:
			return 'stable'
		if failure >= 3:
			return 'die'
# This first loop creates a chain of probabilities

for i in range(trials):
	simulation = death_saves()
	if simulation == 'die':
		die_numb += 1
	elif simulation == 'stable':
		stable_numb += 1
	elif simulation == 'revived':
		revived_numb += 1
# Second loop adds to the count for each simulation

print('die:', die_numb / trials)
print('stabilize:', stable_numb / trials)
print('revive:', revived_numb / trials)