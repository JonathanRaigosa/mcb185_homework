# Skewer 61 by Jonathan Raigosa
'''
import dogma

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')
'''

import sys
import mcb185
import dogma

g_fp = sys.argv[1]
window_size = int(sys.argv[2]) #window size

for defline, seq in mcb185.read_fasta(g_fp):
	for i in range(len(seq) -window_size +1):
		s = seq[i:i+window_size]
		print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')