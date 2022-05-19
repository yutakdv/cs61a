### if문에 3가지 조건 if c, t == False --> else: f?
def if_(c, t, f):
    if  c:
        return t
    else:
        return f
    
from math import sqrt

#### if문 사용의 적절한 예
def real_sqrt(x):
    if x > 0:
        return sqrt(x)
    else:
        return 0.0

#### if문 사용의 부적절한 예
def real_sqrt(x):
    return if_(x > 0, sqrt(x), 0.0)

###conclusion: if문 호출 명령어는 if, else 순으로 쓰는 이유가 괜히 있는게 아니다. -John Denero-
