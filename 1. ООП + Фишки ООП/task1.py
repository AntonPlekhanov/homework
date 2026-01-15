class BankAccount:
     def __init__(self, balance):
          self.__balance = balance


     def deposit(self, amount):
          self.__balance += amount

     def withdraw(self, amount):
          if self.__balance >= amount:
               self.__balance -= amount
          else:
               print('не достаточно средств')
        

     def get_balance(self):
          return self.__balance 
     


# ant = BankAccount(100)
# check = ant.get_balance()
# print(check)

# alex = BankAccount(235)
# check_2 = alex.get_balance()
# print(check_2)

# ant = BankAccount(100)
# check = ant.get_balance()
# print(check)
# ant.deposit(666)
# check_b_af_amount =  ant.get_balance()
# print(check_b_af_amount)

# ant = BankAccount(500)
# print(ant.get_balance())
# ant.withdraw(600)
# check = ant.get_balance()
# print(check)


# a = BankAccount(1000)
# check = a.get_balance()
# print(a.__balance)  #AttributeError: 'BankAccount' object has no attribute '__balance' (ЗАЩИЩЕНО)
# print(a._BankAccount__balance)



