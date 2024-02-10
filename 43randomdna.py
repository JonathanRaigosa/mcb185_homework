# Random DNA by Jonathan Raigosa, received help from lecture.

import random

max_ntlength = 60
min_ntlength = 50
number_seq = 3
nts = 'ACGT'
# setting the main variables

for nt in nts:
	print(nt, end=' ')
print()
# printing nts

for i in range(number_seq):
	print(f'>seq-{i + 1}')
	for j in range(random.randint(min_ntlength, max_ntlength)):
		print(random.choice(nts), end='')
	print()
# taking a random set of integers between 50 and 60
# then, printing a random nucleotide

