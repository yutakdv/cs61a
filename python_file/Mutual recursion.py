#master card 작동 확인 / 10의 배수 == 정상
def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n 
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n 
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

print(luhn_sum(2)) ####answer == 2
print(luhn_sum(32)) ####answer == 8
print(luhn_sum(4)) ####answer == 4
print(luhn_sum(5105105105105100)) ####answer == 20
print(luhn_sum(5461121162798859)) ####answer == 60 // NH농협카드(mastercard)
print(luhn_sum(5327501008707194)) ####answer == 50 // toss체크카드(mastercard)