# 82 transfac by Jonathan Raigosa; Co-author Conner Suen

'''
AC MA0001.3
XX
ID AGL3
XX
DE MA0001.3 AGL3 ; From JASPAR
PO	A	C	G	T
01	0.0	92.0	0.0	3.0
02	0.0	79.0	0.0	16.0
03	82.0	1.0	2.0	10.0
04	40.0	4.0	3.0	48.0
05	56.0	0.0	1.0	38.0
06	35.0	0.0	0.0	60.0
07	65.0	1.0	4.0	25.0
08	25.0	4.0	3.0	63.0
09	64.0	0.0	28.0	3.0
10	0.0	0.0	92.0	3.0
'''

import json
import re
import sys
import gzip

matrices = []
with gzip.open(sys.argv[1], 'rt') as fp:
	record = ''
	for line in fp:
		if line.split()[0] == 'ID':
			info = line.split()[1]
			record = {
				'id': info,
				'pwm': []
			}

		elif re.search('[0123456789]', line.split()[0]):
			n, a, c, g, t = line.split()
			a = float(a)
			c = float(c)
			g = float(g)
			t = float(t)
			counts = {'A': a, 'C': c, 'G': g, 'T': t,}
			record['pwm'].append(counts)
	if record:
		matrices.append(record)
			
print(json.dumps(matrices, indent=4))