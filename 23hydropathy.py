#A function to return the Kyte-Doolitte

def kyte_doolittle_hydrophob(aa):

	if  aa == 'A': 
		return 1.80
	elif aa == 'C':
		return 2.50
	elif aa == 'D':
		return -3.50
	elif aa == 'E':
		return -3.50
	elif aa == 'F':
		return 2.80 
	elif aa == 'G':
		return -0.40
	elif aa == 'H':
		return -3.20
	elif aa == 'I':
		return 4.50
	elif aa == 'K':
		return -3.90
	elif aa == 'L':
		return 3.80
	elif aa == 'M':
		return 1.90
	elif aa == 'N':
		return -3.50
	elif aa == 'P':
		return -1.60
	elif aa == 'Q':
		return -3.50
	elif aa == 'R':
		return -4.50
	elif aa == 'S':
		return -0.80
	elif aa == 'T':
		return -0.70
	elif aa == 'V':
		return 4.20
	elif aa == 'W':
		return -0.90
	elif aa == 'Y':
		return -1.30
	else:
		print('aa is not a valid amino acid.')
		return None

amino_acid = ['A', 'B', 'C', 'T', 'R'] # B is not amino acids

print('A Hydrophobicity is', kyte_doolittle_hydrophob('A'))
print('B Hydrophobicity is', kyte_doolittle_hydrophob('B'))
print('C Hydrophobicity is', kyte_doolittle_hydrophob('C'))
print('T Hydrophobicity is', kyte_doolittle_hydrophob('T'))
print('R Hydrophobicity is', kyte_doolittle_hydrophob('R'))
