def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance    ##important sentence##
        if amount >  balance:
            return 'Insufficient funds.'
        balance = balance - amount    ##local assignment.!! // nonlocal을 쓰지 않을지 local변수로 UnboundLocalError발생.
        return balance
    return withdraw 
 

 printing in vim code. 
 ex) w = make_withdraw(100) 

 #local 함수를 이용하지 않고도 사용 가능
 but 변경 가능한 함수를 생성하기 위해 기존의 변경 가능한 값을 사용할 수 있음 
 ex)
 def make_withdraw_list(balance):
    b = [balance]   ### Name bound outside of withdraw def
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount    ###Element assignment changes a list  
        return b[0]
    return withdraw

withdraw = make_withdraw_list(100)
print(withdraw(25))

#non - local def
??
def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g

a = f(1)
b = a(2)
total = b(3) + b(4) ## b(3) == 10 // b(4) == 12 // total == 22 //// ##review!!

#Environment Diagrams!
def oski(bear):
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [berk + 1, berk - 1]
        bear = lambda ley: berk-ley
        return [berk, cal(berk)]
    return cal(2)

oski(abs) ### answer == [2, [3, 1]]

###nonlocal에 대해서 공부할 것, review!



