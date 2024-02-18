# 53 Genome Stats by Jonathan Raigosa
# test case in 50demo
import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]

gene_lengths = []
exon_lengths = []
cds_lengths = []

with gzip.open(gffpath, 'rt') as gff_fp:
	for line in gff_fp:
		words = line.split('\t')
		if words[2] == feature:
			beg = int(words[3])
			end = int(words[4])
			if feature == 'gene':
				gene_lengths.append(end - beg + 1)
			elif feature == 'exon':
				exon_lengths.append(end - beg + 1)
			elif feature == 'CDS':
				cds_lengths.append(end - beg + 1)
		
# print(feature_len) debug

# Count for Gene, Exon, CDS
gene_count = len(gene_lengths)
exon_count = len(exon_lengths)
cds_count = len(cds_lengths)

print('gene count', gene_count)
print('exon count', exon_count)
print('CDS count', cds_count)

# Minimum for Gene, Exon, CDS
def minimum(find):
	if len(find) == 0:
		return ''
	min_val = find[0]
	for val in find[1:]:
		if val < min_val:
			min_val = val
	return min_val

gene_min = minimum(gene_lengths)
exon_min = minimum(exon_lengths)
cds_min = minimum(cds_lengths)

print('gene minimum', gene_min)
print('exon minimum', exon_min)
print('CDS minimum', cds_min)

# Maximum for Gene, Exon, CDS
def maximum(find):
	if len(find) == 0:
		return ''
	max_val = find[0]
	for val in find[1:]:
		if val > max_val:
			max_val = val
	return max_val

gene_max = maximum(gene_lengths)
exon_max = maximum(exon_lengths)
cds_max = maximum(cds_lengths)

print('gene maximum', gene_max)
print('exon maximum', exon_max)
print('CDS maximum', cds_max)

# Find Mean for Gene, Exon, CDS
def mean(vals):
	if len(vals) == 0:
		return ''	
	mean_total = 0
	for val in vals: mean_total += val
	return int(mean_total / len(vals) + 0.5) # Rounding off number

gene_mean = mean(gene_lengths)
exon_mean = mean(exon_lengths)
cds_mean = mean(cds_lengths)

print('gene mean', gene_mean)
print('exon mean', exon_mean)
print('CDS mean', cds_mean)

# Find STDV for Gene, Exon, CDS
def stdv(vals):
	n = len(vals)
	if n < 2:
		return 0

	mean_val = 0
	for val in vals:
		mean_val += val
	mean_val = mean_val / n

	variance = 0
	for val in vals:
		variance += (val - mean_val) ** 2
	variance = variance / n
	variance = variance ** 0.5
	# print('mean', mean_val)

	# print('before round', variance)
	if variance - int(variance) >= 0.5:
		return int(variance + 1)
	# print('after round', variance)
	return int(variance)

gene_stdv = stdv(gene_lengths)
exon_stdv = stdv(exon_lengths)
cds_stdv = stdv(cds_lengths)

print('stdv gene', gene_stdv)
print('stdv exon', exon_stdv)
print('stdv CDS', cds_stdv)

# Find the Median for Gene, Exon, CDS
def med(vals):
	if len(vals) == 0:
		return 0
	vals.sort()
	n = len(vals)
	if n % 2 == 0: #modular %
		middle_right = n // 2 # integer divide for median
		middle_left = middle_right - 1
		return (vals[middle_left] + vals[middle_right]) / 2
	else:
		return vals[n // 2]

gene_med = int(med(gene_lengths))
exon_med = int(med(exon_lengths))
cds_med = int(med(cds_lengths))

print('gene median', gene_med)
print('exon median', exon_med)
print('cds median', cds_med)