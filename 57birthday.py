# Birthday Program 57 by Jonathan Raigosa

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

total_dups = 0

def duplicates(lst):
	for repeat in lst:
		if repeat > 1:
			return 1
	return 0

for i in range(trials):
	calendar = [0] * days
	for i in range(people):
		bday = random.randint(0, days - 1)
		calendar[bday] += 1
	total_dups += duplicates(calendar)

print(total_dups / trials)