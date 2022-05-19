def make_adder(n): 
    def adder(k):
        return n + k 
    return adder

## secodn make_adder 표현식
def make_adder(n):
    return lambda k: n + k 

#########################
def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

squriple = compose1(square, triple)
print(squriple(4))
#예상 답 = 144 | correct