r = range(3, 6)
list(r)
for i in r:
    print(i)

ri = iter(r)
next(ri)
for i in ri:
    print(i)
#answer == 4, 5 // next(ri)를 사용해서 3이라는 결과값을 도출했으므로 for statement를 사용해 결과값을 도출했을때 4, 5만 출력.

-------reset
r = range(3, 6)
ri = iter(r)
1. for i in ri:
    print(i)
#answer == 3, 4, 5
2. for i in ri:
    print(i)
#answer == _______ // 이미 for statement / iteration를 사용해 결과값을 다 뽑아내서 남아있는 값이 없으므로 출력할게 없음.

#but using just r
for i in r:
    print(r)
 ## printing 3, 4, 5 // every time print it out.

 #Buitl-in Iterator Functions.
 bcd = ['b', 'c', 'd']
 [x.upper() for x in bcd] #['B', 'C', 'D']
 map(lambda x: x.upper(), bcd) #map object 
 --->
 m = map(lmabda x: x.upper(), bcd)
 next(m)
 next(m)
 next(m)

 #vim ex.py 
 def double(x):
    print('**', x, '=>', 2 * x, '**')
    return 2 * x

python3 -i ex.py
map(double, [3, 5, 7]) #map object
m = map(double, [3, 5, 7])
next(m) # ** 3 => 6 **  // except) return 2 * x 
next(m) # ** 5 => 10 ** //    " "
next(m) # ** 7 => 14 **  //   " "

m = map(double, range(3, 7))
f = lambda y: y >= 10
t = filter(f, m)    #map, filter function study, then review !
next(t)
# answer
 ** 3 => 6 **
 ** 4 => 8 **
 ** 5 => 10 **

next(t)
#answer
 ** 6 => 12 **

list(t)
#answer == []

list(filter(f, map(double, range(3, 7))))
#answer 
 ** 3 => 6 **
 ** 4 => 8 **
 ** 5 => 10 **
 ** 6 => 12 **
 [10, 12]


t = [1, 2, 3, 2, 1]
print(t)
reversed(t) #answer == list_reverseiterator object
reversed(t) == t #answer == False
list(reversed(t)) #answer == [1, 2, 3, 2, 1]
list(reversed(t)) == t #answer == True


d = {'a': 1, 'b': 2}
items = iter(d.items())
next(items)
next(items)

items = zip(d.keys(), d.values())
next(items)
next(items)
