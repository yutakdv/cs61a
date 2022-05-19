def count_partitions(n, m):
     if n == 0:
         return 1
     elif n < 0:
         return 0
     elif m == 0:
         return 0
     else:
         with_m = count_partitions(n - m, m)
         without_m = count_partitions(n, m - 1)
         return with_m + without_m
 
result = count_partitions(5, 3)
print(result)
#1 + 1 + 1 + 1 + 1
#1 + 1 + 1 + 2
#1 + 2 + 2
#1 + 1 + 3
#2 + 3
#answer == 5