# 53 Genome Stats by Jonathan Raigosa
# test case in 50demo

import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]

# Minimum
def minimum(find):
	if len(find) == 0:
		return ''
	min_val = find[0]
	for val in find[1:]:
		if val < min_val:
			min_val = val
	return min_val

# Maximum
def maximum(find):
	if len(find) == 0:
		return ''
	max_val = find[0]
	for val in find[1:]:
		if val > max_val:
			max_val = val
	return max_val

# Mean
def mean(vals):
	if len(vals) == 0:
		return ''	
	mean_total = 0
	for val in vals: mean_total += val
	return int(mean_total / len(vals) + 0.5) # Rounding off number

# STDEV
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

# Median	
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

def calcs(gffpath, feature):
	lengths = []
	
	with gzip.open(gffpath, 'rt') as gff_fp:
		for line in gff_fp:
			words = line.split('\t')
			if words[2] == feature:
				beg = int(words[3])
				end = int(words[4])
				lengths.append(end - beg + 1)
	
	# math for Count
	count = len(lengths)
	print(f'{feature} Count:', count)

	if lengths:		
		min_val = minimum(lengths)
		print(f'{feature} Minimum:', min_val)			
			
		max_val = maximum(lengths)
		print(f'{feature} Maximum:', max_val)
	
		mean_val = mean(lengths)
		print(f'{feature} Mean:', mean_val)

		if len(lengths) > 1:			
			stdv_val = stdv(lengths)
			print(f'{feature} STDEV:', stdv_val)	
			
		med_val = med(lengths)
		print(f'{feature} Median:', int(med_val))

calcs(gffpath, feature)