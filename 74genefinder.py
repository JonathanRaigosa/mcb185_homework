# 74 Gene Finder by Jonathan Raigosa; Henry Li; Conner Suen


'''
fasta = sys.argv[1]
threshold = int(sys.argv[2])
'''

'''
123456789
987654321
location_on_forw_strand = len(seq) -location_on_rev_strand +1

'''

import sys
import mcb185

def find_cds(seq, min_orf):
	cds = {}

	for i in range(1, 4):
		while i < len(seq) - min_orf:
			if seq[i:i+3] == 'ATG':
				for j in range(i+3, len(seq)-2, 3):
					if seq[j:j+3] in ['TAA', 'TAG', 'TGA']:
						if j + 2 - i + 1 >= min_orf:
							cds[i+1] = j + 2 + 1
						i = j + 3
						break
			else:
				i += 3

	return cds

min_orf = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defline = defline.split(' ')[0]
	# seq = seq[:10000] debug testing

	CDS_forward = find_cds(seq, min_orf)
	CDS_reverse = find_cds(mcb185.anti_seq(seq), min_orf)

	CDS_all = {}
    
	for start, stop in CDS_forward.items():
		CDS_all[start] = stop
    
	for start, stop in CDS_reverse.items():
		CDS_all[len(seq) - stop + 1] = len(seq) - start + 1
    
	for start, stop in sorted(CDS_all.items(), key=lambda item: item[0]):
		if start in CDS_forward:
			print(f'{defline}\tRefSeq\tCDS\t{start}\t{stop}\t.\t+')
		else:
			print(f'{defline}\tRefSeq\tCDS\t{start}\t{stop}\t.\t-')

'''
for seq_n, seq in mcb185.read_fasta(fasta):
	seq = seq[:3000]
	cds_p(seq_n, seq, threshold)
'''
'''
5'----------------*-M--3' +
3'--M-*----------------5' -
'''
'''
ATG TTA TGC CAT GCC GAG C
A TGT TAT GCC ATG CCG AGC
AT GTT ATG CCA TGC CGA GC
M
		M
'''
# GFF format NC_000913.3	RefSeq	CDS	190	255	.	+


'''
5'ATGTTATGCCATGCCGAGC3' + (19nt)
3'TACAATACGGTACGGCTCG5'	- (19nt)
-------M----------*--
rev strand
M = 6th loc
* = 17th loc

5' to 3'
C = 14th loc corresponding M
G = 3rd loc corresponding *
location_on_forw_strand = len(seq) -location_on_rev_strand +1
'''