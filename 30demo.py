"""
while True:
    print('hello')
"""

i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: break

i = 0
while i < 3:
    print(i)
    i = i + 1
print('final value of i is', i)

#Loop doesn't have to start at 0, increment by 1, or end before 5.
i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)

#for i in range()
#Most loops in Python are for loops, not while loops
for i in range(1, 10, 3):
    print(i)
    
# initial value 1, end limit 10, increment set to 3 ^

for i in range(0, 5):
    print(i)

# Just containing the limit
for i in range(5):
    print(i)
    
    
# for item in container

for char in 'hello':
    print(char)
    
seq = 'GAATTC'
for nt in seq:
    print(nt)
    
# Nested Loops 
for nt1 in 'ACGT':
    for nt2 in 'ACGT':
        if nt1 == nt2: print(nt1, nt2, '+1')
        else:          print(nt1, nt2, '-1')
        
nts = 'ACGT'
for nt1 in nts:
    for nt2 in nts:
        if nt1 == nt2: print(nt1, nt2, '+1')
        else:          print(nt1, nt2, '-1')
        
# Scoring Matrix 
limit = 4
for i in range(0, limit):
    for j in range(i + 1, limit):
        print(i+1, j+1)