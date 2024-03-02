# 65 Transmembrane by Jonathan Raigosa; Young Jaime Class Example.

import dogma
import sys
import mcb185

seq = sys.argv[1]
count = 0 # To count sequences

def hah(seq, window_size, t):
	for i in range(len(seq) -window_size +1):
		tr = seq[i:i+window_size]
		hydro_score = dogma.calc_avg_kd(tr)
		
		if hydro_score >= t and 'P' not in tr:
			return True
	return False

for defline, seq in mcb185.read_fasta(seq): # Young Jaime
	defwords = defline.split(']')
	name = defwords[0]
	if hah(seq[:30], 8, 2.5) and hah(seq[30:], 11, 2.0):
		count += 1 # Count increment
		print(name + ']')

print('Proteins:', count)