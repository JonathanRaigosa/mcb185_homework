# 63 Dust by Jonathan Raigosa; Help from Jordan Shore.

import sys
import dogma
import mcb185

gff_file = sys.argv[1]
window_size = int(sys.argv[2])
entropy_threshold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(gff_file):
	nts = list(seq)
	#print(nts)
	for i in range(0, len(seq) - window_size + 1):
		subseq = seq[i:i+window_size]
		acount = subseq.count('A') # Counts the Nts sequence
		ccount = subseq.count('C')
		gcount = subseq.count('G')
		tcount = subseq.count('T')
		entropy = dogma.shannon_entropy(acount, ccount, gcount, tcount)
		if entropy < entropy_threshold:
			for j in range(i, i + window_size):
				nts[j] = 'N' # Masking Sequence
	final_seq = ''.join(nts)
	print(f'> {defline}')
	for i in range(0, len(final_seq), 60):
		print(final_seq[i:i+60])