# ColorName by Jonathan Raigosa

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

distance_max = 1000000

def dtc(P, Q): # list P and Q
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d
# From MCB185 module 5
def color_close(colorfile, target):
	closest_name = ''
	closest_dist = distance_max
	
	with open(colorfile, 'rt') as fp:
		for line in fp:
			line_parts = line.split('\t')
			color_name = line_parts[0]
			r, g, b = line_parts[2].split(',')
			r = int(r)
			g = int(g)
			b = int(b)
			
			
			
			dist = dtc(target, (r, g, b)) # R, G, B are the values I input
			
			if dist < closest_dist: # takes the closest integers
				closest_dist = dist # sets them equal
				closest_name = color_name #reads line_parts[0]
	
	return closest_name

print(color_close(colorfile, [R, G, B]))
