odds = [3, 5, 7 ,9, 11]
list(range(1, 3)) # [1. 2]
[odds[i] for i in range(1, 3)] # [5, 7]
odds[1: 3] # [5, 7]
odds[:3] # [5, 7]
odds[1:] # [3, 5, 7, 9, 11]
odds[:] # [3, 5, 7 ,9, 11]

sum([2, 3, 4])
sum(['2', '3', '4']) # TypeError: 'int + 'str'
sum([2, 3, 4], 5) # 14 
[2, 3] + [4]
sum([[2, 3], [4]], []) # [2, 3, 4]
sum([[2, 3], [4]]) # TypeError; 'int' + 'list'
[] + [2, 3] + [4] #[2, 3, 4]

max(range(5))
max(0, 1, 2, 3, 4)
max(range(10), key = lambda x: 7-(x-4)*(x-2)) ## key를 활용해 중요값임을 표시
#check
(lambda x: 7-(x-4)*(x-2))(3) # 8
(lambda x: 7-(x-4)*(x-2))(2) # 7
(lambda x: 7-(x-4)*(x-2))(4) # 7
(lambda x: 7-(x-4)*(x-2))(5) # 4
(lambda x: 7-(x-4)*(x-2))(6) # -1

#bool
[x < 5 for x in range(5)] ##[True, True, True, True, True]
all(x < 5 for x in range(5)) ##True
all(range(5)) ##False, reason: range(5) --> range(0, 5)