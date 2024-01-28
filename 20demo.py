# 20demo.py by Jonathan_Raigosa

print('hello again') # greeting

# Tabs on the left
# Spaces on the right
# Need tabs for your if statements

# Math

import math

print(1.5e-2)
print(1 + 1)
print(1 - 1)
print(2 * 2)
print(1 / 2)
print(2 ** 3)
print(5 // 2)
print(5 % 2)
print(5 * (2 + 1))
print(math.pow(2, 3))
print(2 ** 0.5)
print(math.sqrt(2))
print(math.log(2))
print(0.1 * 1)
print(0.1 * 3)

# Variable
a = 3           # Side of Triangle
b = 4           # Side of Triangle
c = math.sqrt(a**2 + b**2)
print(c)

# Type

print(type(a), type(b), type(c), sep=', ')

# Functions

def greeting():
    print('hello Jonathan Raigosa')

# Example

def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

x = pythagoras(3, 4)
print(x)

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)
    
print(pythagoras(3, 4))
print(pythagoras(1, 1))

# assert() and sys.exit()

"""
def pythagoras(a, b):
    assert(a > 0)
    assert(b > 0)
    return math.sqrt(a**2 + b**2)

print(pythagoras(-1, 1))

import sys

def pythagoras(a, b):
    if a <= 0: sys.exit('error: a must be greater than 0')
    if b <= 0: sys.exit('error: b must be greater than 0')
    return math.sqrt(a**2 + b**2)
"""
# Practice
def invert_sign(number):
    return abs(number)

result = invert_sign(-5)
print(result)

#strings

s = 'hello world'
print(s, type(s))

#Conditional

a = 3
b = 2
if a == b:
    print('a equals b')

if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')