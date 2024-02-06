# Choosek by Jonathan Raigosa # Help from Yutong Ji

def factor(n):
	if n == 0: return 1
	fact = 1
	for i in range(1, n + 1):
		fact = fact * i
	return fact

def answer(n, j):
	return factor(n) // factor(j) // factor(n - j)

print(answer(5, 2))
print(answer(12, 3))
print(answer(10, 3))
