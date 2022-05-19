def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

print(cascade(123)) 
####answer####
"""
123
12
1
12
123
""" 

## using if code
def cascade(n):
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)

print(cascade(12345))
####answer####
"""
12345
1234
123
12
1
12
123
1234
12345
"""

####inverse_cascade####
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)
    
grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)

print(inverse_cascade(1234))
####answer####
"""
1
12
123
1234
123
12
1
"""


#print에서 none을 활용!
#none값은 출력하지 않는다. 