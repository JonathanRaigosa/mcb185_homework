# Choosek by Jonathan Raigosa

def factor(n):
	if n == 1 or n == 0:
		return 1
	else: 
		return n * factor(n - 1)

def answer(n, i):
	if i < 0 or i > n:
		return 0
	else:
		return factor(n) // factor(i) * factor(n - i)

print(answer(8, 4))
print(answer(12, 8))
print(answer(14, 2))
