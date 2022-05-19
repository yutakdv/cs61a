""" Generalization """

def identity(k):
    return k

def cube(k):
    return pow(k,  3)

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    return summation(n, identity)

def sum_cube(n):
    return summation(n, cube)

### sum_naturals == 수열 합
### sum_cube == 세제곱 수열의 합

print(sum_naturals(5))
print(sum_cube(5))