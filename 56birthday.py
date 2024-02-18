# Birthday Program 56 by Jonathan Raigosa received help from peer

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

total_prob = 0

for i in range(trials):
	dup = 0
	bdays = list()

	for i in range(people):
		bday = random.randint(1, days)
		if bday in bdays:
			dup += 1
			# print('Duplicate') was for debugging
# meant to see the Duplicates experienced in a smaller list
		bdays.append(bday)
	if dup > 0:
		total_prob += 1

print(total_prob / trials)