# Fibonacci Sequence by Jonathan Raigosa

def fib_sequence(n):
	x1 = 0 
	x2 = 1
# First two numbers of the Fib sequence

	for i in range(n):
		xfinal = x1 + x2
		print(x1)
		x1 = x2
		x2 = xfinal
		
fib_sequence(10)

