class BankAccount:
  def __init__(self,acc_no,acc_name,initial_bal=0.0):
    self.__acc_no=acc_no
    self.__acc_name=acc_name
    self.__acc_bal=initial_bal
  def deposit(self,amount):
     if amount > 0:
        self.__acc_bal += amount 
        print("Deposited ₹ {}. New Balance : ₹{}".format(amount,self.__acc_bal))
     else:
        print("Invalid amount. Please deposit a positive amount ")
  def withdraw(self,amount):
     if amount > 0 and amount <= self.__acc_bal:
        self.__acc_bal -= amount
        print("withdrawn ₹{}. New balance: ₹{}".format(amount, self.__acc_bal))
     else:
        print("Invalid withdrawal amount or insufficient balance")
  def display(self):
       print("Account balance for {}(Account no = {} : ₹ {}".format(self.__acc_name,self.__acc_no,self.__acc_bal))
account = BankAccount(acc_no="10002345",acc_name="Amelia", initial_bal=50000)
account.display()
account.withdraw(1000.0)
account.deposit(1000.0)