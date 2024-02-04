# Scoring Matrix by Jonathan Raigosa

sequence = 'ACGT'
print('   ', end=' ')
# Print provides a space and terminates

for i in sequence:
	print(i, end='  ')
print()

for seq_1 in sequence:
	print(seq_1, end='  ')
	for seq_2 in sequence:
		if seq_1 == seq_2: print('+1', end=' ')
		else: print('-1', end=' ')
	print()
	

# The spaces are required for the matrix spacing.

