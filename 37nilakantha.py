# nilakantha.py by Jonathan Raigosa (estimating pi)

def pi_estimate(nilakantha):
	sign_flip = 1
	estimation = 3

	for i in range(1, nilakantha):
		denom = 2 * i * (2 * i + 1) * (2 * i + 2)
# First Expression for the denominator
		
		equation = 4 / denom
# general layout
		
		estimation = estimation + (sign_flip * equation)
# sign is flipped in series

		sign_flip = sign_flip * -1
# If the sign flip comes before the estimation cal,
# then the number pushes 2.8, if it is after 3.14

	return estimation

print(pi_estimate(100))
print(pi_estimate(5))
print(pi_estimate(1))
# The bigger the printed number! The more accurate the value of pi.