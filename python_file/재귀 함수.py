def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n 
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

#same code
def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum

#upgrade code
def sum_digits_rec(n, digit_sum):
     if n == 0:
         return digit_sum
     else:
         n, last = split(n)
         return sum_digits_rec(n, digit_sum + last)
    
print(sum_digits(2013)) #### answer == 6
print(sum_digits(123456789)) ### answer == 45

print(sum_digits_iter(2013)) #### answer == 6
print(sum_digits_iter(123456789)) #### answer == 45

print(sum_digits_rec(32, 4)) #### answer == 9
print(sum_digits_rec(32, 5)) #### answer == 10
print(sum_digits_rec(0, 4)) #### answer == 4