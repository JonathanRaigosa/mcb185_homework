# Jonathan Raigosa, Co Author Kobe Goliman

def pi_estimate(pi):
	sign_flip = 1
	start = 4

for i range(pi):
	gl_denom = (1 + (2 * i))
	gl = 4 / gl_denom
	sign_flip = sign_flip * (-1)
	start = start + (sign_flip * gl)
print(gl)