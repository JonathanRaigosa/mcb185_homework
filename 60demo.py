# 60demo.py by Jonathan Raigosa

import sys
import mcb185

'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	A = 0
	C = 0
	G = 0
	T = 0
	N = 0
	for nt in seq:
		if nt == 'A': A += 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else:			N += 1
	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
'''


'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN'
	counts = []
	for i in range(len(nts)): counts.append(0)
	for nt in seq:
		if nt == 'A': counts[0] += 1
		elif nt == 'C': counts[1] += 1
		elif nt == 'G': counts[2] += 1
		elif nt == 'T': counts[3] += 1
		else:			counts[4] += 1
	print(name, end='\t')
	for n in counts: print(f'{n/len(seq):.4f}', end='\t')
	print()
# List Variation
'''

'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN'
	counts = [0] * len(nts)
	for nt in seq:
		idx = nts.find(nt)
		counts[idx] += 1
	print(name, end='\t')
	for n in counts: print(f'{n/len(seq):.4f}', end='\t')
	print()
# Indexing with str.find()
'''

'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN'
	print(name, end='\t')
	for nt in nts:
		print(seq.count(nt) / len(seq), end='\t')
	print()
# Counting with str.count()
'''
'''
# Sliding WIndow Algorithms
w = 10
s = 1
for i in range(0, len(seq) -w +1, s):
	subseq = seq[i:i+w]
'''


for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print("defline:", defline)
    print("seq:", seq)
    if defline is not None:
        defwords = defline.split()
        name = defwords[0]
        nts = 'ACGTN'
        counts = [0] * len(nts)
        for nt in seq:
            idx = nts.find(nt)
            counts[idx] += 1
        print(name, end='\t')
        for n in counts: print(f'{n/len(seq):.4f}', end='\t')
        print()
    else:
        print("Warning: Encountered a None value for defline. Skipping this entry.")
