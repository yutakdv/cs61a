def print_all(x):  
    print(x)
    return print_all

print(print_all(1)(2)(3))    ##### 예상 정답: 1 2 3

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum

print(print_sums(1)(3)(5))   ##### 예상 정답: 1 4 9