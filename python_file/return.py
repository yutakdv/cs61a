##1. 반복함수 사용 <True>
def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

##2. 반복함수 사용 <Not f(x)>
def search(f):
        x = 0
        while not f(x):
            x += 1
        return x
        
## 1, 2 logic == same

def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

### 💯역함수 사용 표현💯 ###
def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y: search(lambda x: f(x) == y)