#Iterator / next
s = [3, 4, 5]
t = iter(s)
next(t)
next(t)
next(t)
 ----- 
 u = iter(s)
 next(u)
 next(u)
 next(u)

s = [[1, 2], 3, 4, 5]
next(s) == TypeError  #'list' object is not an iterator!
t = iter(s)
next(t) == [1, 2] 
next(t) == 3
list(t) == [4, 5]
next(t) == StopIteration #no more value 
