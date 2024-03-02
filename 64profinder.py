# 64 Profinder by Jonathan Raigosa, Worked with Lilith

'''
Example with Lilith
for aa in aaseq:

	if aa == 'M'
		if started:
			if aa == '*' and len(protein) >= 100:
				print(''.join(protein))
				protein = []
				started = False
				# Check conditions.
			else:
				# add the amino acid and move
				protein.append(aa)
		elif aa == 'M':
			started = True
			protein.append(aa)
'''

import sys
import mcb185
import dogma

seq = sys.argv[1]
window_size = int(sys.argv[2])

def profinder(seq, window_size):

	proteins = [] # stores protein sequence
	translation = [] # stores translated amino acid seq

	for sixframe in range(3):
		forward = dogma.translate_master(seq[sixframe:]) # 0, 1 and 2 forward and rev frames translate
		translation.append(forward)
		reverse = dogma.translate_master(dogma.revcomp(seq)[sixframe:])
		translation.append(reverse)

	for translate in translation: # Done with Lilith

		aas_list = []
		start_found = False

		for aa in translate:
			if start_found:
				if aa == '*':
					if len(aas_list) >= window_size:
						proteins.append(''.join(aas_list))
					aas_list = []
					start_found = False
				else:
					aas_list.append(aa)
			elif aa == 'M':
				start_found = True
				aas_list.append(aa)

	return proteins

for defline, seq in mcb185.read_fasta(seq): # Work on this
	#print(f'Process sequence: {defline}') # Debug
	count = 0
	for protein in profinder(seq, window_size):
		print(f'>{defline}-prot-{count}\n{protein}')
		count += 1