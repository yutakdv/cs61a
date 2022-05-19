#recursion(재귀함수) #using 'if'
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(3)) ####answer == 6
print(fact(5)) ####answer == 120

#iteration(반복함수) #using 'while'
def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

print(fact_iter(3)) ####answer == 6
print(fact_iter(5)) ####answer == 120