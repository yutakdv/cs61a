### pred, curr = 0, 1 and k = 1 (first case)
def fib(n):
    pred, curr = 0, 1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr

print(fib(1))  # 1
print(fib(5))  # 5
print(fib(10)) # 55

### if pred, curr = 1, 0 and k = 0 (second case)--> what happen this code?
def fib(n):
    pred, curr = 1,0
    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr

print(fib(1))
print(fib(5))
print(fib(10))

###pred, curr = 1, 0 // k = 0 || pred, curr 0, 1 // k = 1 == same result 

####another fibonadci number code / using 'if' // 위 함수보다 계산하는데 더 오래걸림
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
print(fib(1))
print(fib(5))
print(fib(10))

