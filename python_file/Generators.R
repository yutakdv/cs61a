def plus_minus(x):
    yield x
    yield -x

t = plus_minus(3)
next(t)
next(t)
t # generator object plus_minus ...

# A generator function is a functino that yields values instead of returning them
# A normal function returns once; a generator function can yield multiple times
# A generator is an iterator created automatically by calling a generator function
# When a generator function is called, it returns a generator that iterates over its yields

## Studying yield, then review 

#vim ex.py
def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

#python3 -i ex.py
t = evens(2, 10)
t # generator object evens a...
next(t)
next(t)
next(t)

list(evens(2, 10))
t = evens(2, 10)
next(t)
next(t)


# Generators & Iterators
#Gerators can yield from Iterators
#-A yield from statement yields all values from an iterator or iterable 


#code
def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x

#same code
def a_then_b(a, b):
    yield from a
    yield from b

list(a_then_b([3, 4], [5, 6])) # [3, 4, 5, 6]

#--------------#

#code
def countdown(k):
    if k > 0:
        yield k 
        yield countdown(k - 1)

t = countdown(3)
next(t) #answer == 3
next(t) #guess get back 2 // but print <generator object countdown at ...>
#--> change code

list(countdown(5)) # [5, 4, 3, 2, 1]

#code
def countdown(k):
    if k > 0:
        yield k
        for x in countdown(k - 1):
            yield x

#again
t = countdown(3)
next(t) #answer == 3
next(t) #answer == 2
next(t) #answer == 1

#same code -> for x in countdown(k - 1)
def countdown(k):
    if k > 0:
        yield k 
        yield from countdown(k - 1)
    else:  ### 그냥 멋짐을 위해 추가함.. -> John Denero 교수가...
        yield 'Blast off'

for k in countdown(3):
    print(k)

#answer
#3
#2
#1
#Blast off

#------------#
#vim ex.py
def countdown(k):
    if k > 0:
        yield k 
        yield from countdown(k - 1)
    else:
        yield 'Blast off'

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

#python3 -i ex.py
prefixes('both') #answer == <generator object prefixes at ...>
list(prefixes('both')) #answer == ['b', 'bo', 'bot', 'both']

#plus vim code
def countdown(k):
    if k > 0:
        yield k 
        yield from countdown(k - 1)
    else:
        yield 'Blast off'

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

#python3 -i ex.py
substrings('tops') #ansewr == <generator object substrings at ...>
list(substrings('tops')) #answer == ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
