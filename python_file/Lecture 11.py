def count(s, value):
    total, index = 0, 0
    while index < len(s):
        element = s[index]

        if element == value:
            total += 1

        index += 1
    return total

print(count([1, 2, 1, 2, 1], 1)) #####answer == 3

def count(s ,value):
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

print(count([1, 2, 1, 2, 1], 1)) #####answer == 3 

pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
same_count = 0
for x, y in pairs:
    if x == y:
        same_count += 1

print(same_count) #####answer == 2

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(sum_below(5)) #####answer == 10

def cheer():
    for _ in range(3):     #### _ 대신 x, y 등 다른 미지수 써도 상관없음.
        print('Go Bears!')

print(cheer()) #####answer == Go Bears! 
               #####          Go Bears!
               #####          Go Bears!

odds = [1, 3, 5, 7, 9]
print([x + 1 for x in odds]) ######answer == [2, 4, 6 ,8 , 10]
print([x for x in odds if 25 % x == 0]) #####answer == [1, 5]
print([x + 1 for x in odds if 25 % x == 0]) #####answer == [2, 6]

def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

print(divisors(1)) #####answer == [1]
print(divisors(4)) #####answer == [1, 2]
print(divisors(8)) #####answer == [1, 2, 4]
print(divisors(12)) #####answer == [1, 2, 3, 4, 6]
print(divisors(18)) #####answer == [1, 2, 3 , 6 , 9]

#Upgrade code #우리가 아는 '약수' 구하는 코드 
def divisors(n):
    return [1] + [x for x in range(2, n + 1) if n % x == 0]

print(divisors(1)) #####answer == [1]
print(divisors(4)) #####answer == [1, 2, 4]
print(divisors(8)) #####answer == [1, 2, 4, 8]
print(divisors(12)) #####answer == [1, 2, 3, 4, 6, 12]
print(divisors(18)) #####answer == [1, 2, 3 , 6 , 9, 18]

'curry = lambda f: lambda x: lambda y: f(x, y)' ###just string
exec('curry = lambda f: lambda x: lambda y: f(x, y)')
#print(curry) #####answer == <function <lambda> at 0x100a16830>

exec('curry = lambda f: lambda x: lambda y: f(x, y)')
from operator import add
#print(curry(add)(3)(4)) ######answer == 7