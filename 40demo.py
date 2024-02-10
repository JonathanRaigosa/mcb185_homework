# Demo Code for HW 4 by Jonathan Raigosa

import random
# random number generators are essential for random expectations as a background model or null hypothesis

random.random()
# produces a number 0 <= X < 1.

for i in range(5):
	print(random.random())
# prints 5 random numbers

for i in range(50):
	print(random.choice('ACGT'), end='')
print()
# this randomly chooses an item from our container.

for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='')
	else:		print(random.choice('CG'), end='')
# prints 70% 'AT' and 30% 'CG'

for i in range(3):
	print(random.randint(1, 6))
# random.randint() generates a random # betwween two inclusive end points. Like simulating a 6 sided dice.

for i in range(5):
	print(random.gauss(0.0, 1.0))
# random library supports several common distributions, like the Gaussian (normal) distribution. Mean and Standard Deviation

print('this line\n has some\n line breaks')
print('a\tb\tcat\tdogma')
# Returns to next line \n & inserts tab \tab

print(10, 20, 30, 40, sep='\t')
print(100, 2000, 30000, 40000, sep='\t')