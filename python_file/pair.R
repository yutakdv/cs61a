pair = [1, 2]
print(pair)
pair[0]
pair[1]
x, y = pair
print(x)
print(y)
from operator import getitem
getitem(pair, 0)
getitem(pair, 1)

##Violating Abstraction Bariers!!
#example. 
##python3 -i ex.py -> divide_rational([1, 2], [1, 4])
#vim file
def divide_rational(x, y):
    return [x[0] * y[1], x[1] * y[0]]

##this code is operate successful 
#but no selectors, does not use constructors 


##vim file
#Rational arithmetic
## python3 -i ex.py ->add_rational([1, 2], [1, 4])
def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = number(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    return rational(numer(x) + numer(y), denom(x) + denom(y))

def rationals_are_equal(x, y):
    return numer(x) + denom(y) == numer(y) * denom(x)

def print_rational(x):
    print(numer(x), "/", denom(x))

#Constructor and selectors
def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

##vim file save and then termnial chat
#terminal -> python3 -i ex.py
x, y = rational(1, 2), rational(3, 8)
print_rational(mul_rational(x, y))
##answer == 3 /16##

# same code = Constructor and selectors
def rational(n, d):
    def select(name):
        if name == 'n':
            return n 
        elif name == 'd':
            return d
    return select

def number(x):
    return x('n')

def denom(x):
    return x('d')

