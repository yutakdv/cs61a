class Clown:
    nose = 'big and red'
    def dance():
        return 'No thanks'

print(Clown.nose) ##'big and red'
print(Clown.dance()) ##'No thanks'

###
class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

a = Account('Jim')
b = Account('Jack')
print(a.holder) ## Jim
print(a.balance) ## 0 
print(b.holder) ## Jack

###
class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds.'
        self.balance = self.balance - amount
        return self.balance

tom_account = Account('Tom')
print(tom_account.deposit(100))

print(Account) ## <class ' __main__.Account'>
john = Account('John')
type(john) ## <class ' __main__.Account'>
print(john.balance) ## 0
print(john.holder) ## 'John'
print(john.deposit(10)) ## 10
print(john.deposit(10)) ## 20
print(john.deposit(10)) ## 30
print(john.balance) ## 30
print(john.withdraw(30)) ## 0
print(john.withdraw(30)) ## 'Insufficient funds.'

print(getattr) ## <built-in function getattr>
print(getattr(john, 'balance')) ## 0
print(john.deposit(100)) ## 100
print(getattr(john, 'balance')) ## 100
print(john.balance) ## 100
print(hasattr(john, 'balance')) ## True
print(hasattr(john, 'lance')) ## False

print(type(Account.deposit)) ## <class 'function'>
print(type(tom_account.deposit)) ## <class 'method'>

#two methods.
#1.
print(Account.deposit(tom_account, 1001))
#2.
print(tom_account.deposit(1000))

###
class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    
tom_account = Account('Tom')
jim_account = Account('Jim')
print(tom_account.interest) ## 0.02
print(jim_account.interest) ## 0.02


###midterm Review Question###
def combo(a, b):
    """Return the smallest integer with all of the digits of a and b (in order).
    
    >>>combo(531, 432)        # 45312 contains both _531_ and 4_3_2.
    45312
    >>>combo(531, 4321)       # 45321 contains both _53_1 and 4_321.
    45321
    >>>combo(1234, 9123)      # 91234 contains both _1234 and 9123_.
    91234
    >>>combo(0, 321)          # The number 0 has no digits, so 0 is not in the result.
    321
    """

###Write code
    if a == 0 or b == 0:
        return a + b
    elif a % 10 == b % 10:
        return combo(a // 10, b // 10) * 10 + a % 10
    return min(combo(a // 10, b) * 10 + a % 10, combo(a, b // 10) * 10 + b % 10)   

#<expression>.<name>
#classs <name>(<base class>):
#   <suite>

class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    whitdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

#Base class attributes aren't copied into subclasses!

a = Account('John')
b = CheckingAccount('Jack')
print(a.balance)
print(b.balance)
print(a.deposit(100))

