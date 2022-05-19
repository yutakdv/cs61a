d = {'one': 1, 'two': 2, 'three': 3}
d['zero'] = 0
k = iter(d.keys()) #iter(d) // same 
next(k)
next(k)
next(k)

v = iter(d.values())
next(v)
next(v)
next(v)

i = iter(d.items())
next(i)
next(i)
next(i)

d = {'one': 1, 'two': 2}
k = iter(d)
next(k)
d['zero'] = 0
next(k) #RuntimeError == dictionary changed size during iteration // k를 사용하는 동안 사전이 변경되었기 때문에 k를 더 이상 사용 불가.!
## if change it, make new one / then okay
print(d)
k = iter(d)
next(k)
next(k)
d['zero'] = 5 
next(k)


{'I': 1, 'V': 5, 'X': 10}
numerals = {'I': 1, 'V': 5, 'X': 10}
#1. print(numerals)
#2. print(numerals['X']) ### printing value  
#3. print(numerals.keys()) ### just printing keys
#4. print(numerals.values()) ### just printing values
#5. print(numerals.items()) ### print {keys, value} in dictionary


items = [('X', 10), ('V', 5), ('I', 1)]
#1. print(items) ### print items
#2. print(dict(items)) ### using dict -> dict funciton
#3. print(dict(items)['X']) ### using dict -> print value == 10
#4. print('X' in numerals) ### True
#5. print('X-ray' in numerals) ### False
#6. print(numerals.get('X', 0)) ### using get function -> 10
#7. print(numerals.get('X-ray', 0)) ### using get function -> but no 'X-ray' key -> 0


print({x: x * x for x in range(10)})

squares = {x: x * x for x in range(10)}
print(squares[7])

# dict function can't get two same keys 
# if True -> one is get out
# example
# Wrong function #
# {1: 2, 1: 3}
# Right function #
# {1: [2, 3]} ## [2, 3] value is just a sequence so no problem
# {[1]: 2} ## TypeError: unhashable type: 'list' #key can't get a list? 
