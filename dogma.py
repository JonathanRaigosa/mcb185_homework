# Dogma by Jonathan Raigosa
import math

def transcribe(dna):
	return dna.replace('T', 'U')
	
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:			rc.append('N')
	return ''.join(rc)

'''
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		else:				aas.append('X')
	return''.join(aas)
'''

def translate(dna):
	codons = ('ATG', 'TAA')
	aminos = 'M*'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			idx = codons.index(codon)
			aa = aminos[idx]
			aas.append(aa)
		else:
			aas.append('X')
	return ''.join(aas)

def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

def shannon_entropy(acount, ccount, gcount, tcount):
	total = acount + ccount + gcount + tcount


	if total == 0:
		return 0 # If there are not nt, then entropy is zero

# Calculation of probabilities

	prob_a = acount / total if acount > 0 else 0
	prob_c = ccount / total if ccount > 0 else 0
	prob_g = gcount / total if gcount > 0 else 0
	prob_t = tcount / total if tcount > 0 else 0
	
	

# Calculating Entropy using Shannon's Entropy

	entropy = -(prob_a * math.log2(prob_a)) if prob_a > 0 else 0
	entropy += -(prob_t * math.log2(prob_t)) if prob_t > 0 else 0
	entropy += -(prob_g * math.log2(prob_g)) if prob_g > 0 else 0
	entropy += -(prob_c * math.log2(prob_c)) if prob_c > 0 else 0


	return entropy

def translate_master(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TTT': aas.append('F')
		elif codon == 'TTC': aas.append('F')
		elif codon == 'TTA': aas.append('L')
		elif codon == 'TTG': aas.append('L')
		elif codon == 'TCT': aas.append('S')
		elif codon == 'TCC': aas.append('S')
		elif codon == 'TCA': aas.append('S')
		elif codon == 'TCG': aas.append('S')
		elif codon == 'TAT': aas.append('Y')
		elif codon == 'TAC': aas.append('Y')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGT': aas.append('C')
		elif codon == 'TGC': aas.append('C')
		elif codon == 'TGA': aas.append('*')
		elif codon == 'TGG': aas.append('W')
		elif codon == 'CTT': aas.append('L')
		elif codon == 'CTC': aas.append('L')
		elif codon == 'CTA': aas.append('L')
		elif codon == 'CTG': aas.append('L')
		elif codon == 'CCT': aas.append('P')
		elif codon == 'CCC': aas.append('P')
		elif codon == 'CCA': aas.append('P')
		elif codon == 'CCG': aas.append('P')
		elif codon == 'CAT': aas.append('H')
		elif codon == 'CAC': aas.append('H')
		elif codon == 'CAA': aas.append('Q')
		elif codon == 'CAG': aas.append('Q')
		elif codon == 'CGT': aas.append('R')
		elif codon == 'CGC': aas.append('R')
		elif codon == 'CGA': aas.append('R')
		elif codon == 'CGG': aas.append('R')
		elif codon == 'ATT': aas.append('I')
		elif codon == 'ATC': aas.append('I')
		elif codon == 'ATA': aas.append('I')
		elif codon == 'ACT': aas.append('T')
		elif codon == 'ACC': aas.append('T')
		elif codon == 'ACA': aas.append('T')
		elif codon == 'ACG': aas.append('T')
		elif codon == 'AAT': aas.append('N')
		elif codon == 'AAC': aas.append('N')
		elif codon == 'AAA': aas.append('K')
		elif codon == 'AAG': aas.append('K')
		elif codon == 'AGT': aas.append('S')
		elif codon == 'AGC': aas.append('S')
		elif codon == 'AGA': aas.append('R')
		elif codon == 'AGG': aas.append('R')
		elif codon == 'GTT': aas.append('V')
		elif codon == 'GTC': aas.append('V')
		elif codon == 'GTA': aas.append('V')
		elif codon == 'GTG': aas.append('V')
		elif codon == 'GCT': aas.append('A')
		elif codon == 'GCC': aas.append('A')
		elif codon == 'GCA': aas.append('A')
		elif codon == 'GCG': aas.append('A')
		elif codon == 'GAT': aas.append('D')
		elif codon == 'GAC': aas.append('D')
		elif codon == 'GAA': aas.append('E')
		elif codon == 'GAG': aas.append('E')
		elif codon == 'GGT': aas.append('G')
		elif codon == 'GGC': aas.append('G')
		elif codon == 'GGA': aas.append('G')
		elif codon == 'GGG': aas.append('G')
		else:				aas.append('X')
	return ''.join(aas)

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
		return 0

def calc_avg_kd(sequence):
	tot_kd = 0
	for aa in sequence:
		tot_kd += kyte_doolittle_hydrophob(aa)
	return tot_kd / len(sequence)
		