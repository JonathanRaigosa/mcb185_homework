# Demo 50 by Jonathan Raigosa.

# test set for 53genomestats.py
length = [120, 230, 530, 670]

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
	return int(variance + 1)
print(stdv(length))

# string is a container that holds letters 
seq = 'GAATTC'
print(seq[0], seq[1])

# indexes can be negative and count backwards from right
print(seq[-1])

# looping 
for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
# Slices = subset of a contaner

s = 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])
# starting 0, 

tax = ('Homo', 'sapiens', 9606) # construct tuple
print(tax)						# note the parentheses in the output



print(tax[0])	# index
print(tax[::-1])# slice

#tuple is for a function
def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2
	
x1, x2 = quadratic(5, 6, 1)			#unpacked tuple - yes
print(x1, x2)						# pretty
intercepts = quadratic(5, 6, 1)		# packed tuple - NO!
print(intercepts[0], intercepts[1]) #ugly


# enumerate() and zip()

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

#zip()

names = ('adenine', 'ctyosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
# Lists

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

# sort elements
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# list() you don't know how big they are Variable

items = list()
print(items)
items.append('eggs')
print(items)

#empty list
stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIJKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)
