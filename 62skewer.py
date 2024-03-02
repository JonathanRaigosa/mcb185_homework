# 62 Skewer by Jonathan Raigosa Only Slightly Faster
# ; Help from Ian Korf Lecture

import sys
import mcb185
import dogma

g_fp = sys.argv[1]
window_size = int(sys.argv[2]) #window size

for defline, seq in mcb185.read_fasta(g_fp):
	g = seq[0:window_size].count('G')
	c = seq[0:window_size].count('C')
	for i in range(len(seq) - window_size):
		off = seq[i]
		on = seq[i+window_size]
		
		if off == 'C': c -= 1
		elif off == 'G': g -= 1
		
		if on == 'C': c += 1
		elif on == 'G': g += 1
		
		comp = (c + g) / window_size
		
		if (g + c) > 0: skew = (g - c) / (g + c)
		else:			skew = 0

		print(i, comp, skew)