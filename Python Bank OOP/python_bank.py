
# This program illustrates all the OOP concepts learned uptil now

import datetime


class BankDB:
    accountDB = []

    def __init__(self, name, handphone, password, balance=0):
        self.name = name
        self.ID = handphone
        self.password = password
        self.balance = balance

    def __repr__(self):
        return 'welcome to Bank Python Database'

    def register(self):
        BankDB.accountDB.append({'name': self.name, 'ID': self.ID, 'password': self.password, 'balance' : self.balance})
        
        
class BankAccount(BankDB):			# inheritance from BankDB

    def __init__(self, ID, password):
        super().__init__(self, ID, password)	# inheritance from BankDB

        self.loginStatus= 0
        
        for data in BankDB.accountDB:
            if self.ID == data['ID'] and self.password == data['password']:
                self.index = BankDB.accountDB.index(data)
                self.name = data['name']
                # self.ID = data['ID']
                # self.password = data['password']
                self.balance = data['balance']
                self.loginStatus= 1
                print(f"Login Success, Welcome to Python Bank '{self.name}'")
                print('')
                return
        print('Wrong ID or Password')
        print('')

    def __repr__(self):
        if self.loginStatus == 1:
            return f"Name = '{self.name}', ID = '{self.ID}'\n"

    def myBalance(self):
        if self.loginStatus == 1:
            print(f"customer name     : {self.name}")
            print(f"your balance now  : {BankDB.accountDB[self.index]['balance']}")
            print('')
            return
        print("Error, Please Login")
        return

    def deposit(self, amount):
        if self.loginStatus == 1:
            self.balance += amount
            BankDB.accountDB[self.index]['balance'] = self.balance
            print(f"customer name     : {self.name}")
            print(f"transaction time  : {datetime.datetime.now()}")
            print(f"deposit  (^_^)    : {amount}")
            print(f"your balance now  : {self.balance}")
            print('')
            return
        print("Error, Please Login")
        return

    def withdraw(self, amount):
        if self.loginStatus == 1:
            if self.balance < amount:
                print(f"customer name     : {self.name}")
                print(f"your balance      : {self.balance}")
                print(f"withdraw          : {amount}")
                print('withdraw failed   : Not enough balance!')
                print('')
                return
            else:
                self.balance -= amount
                BankDB.accountDB[self.index]['balance'] = self.balance
                print(f"customer name     : {self.name}")
                print(f"transaction time  : {datetime.datetime.now()}")
                print(f"withdraw (T-T)    : {amount}")
                print(f"your balance now  : {self.balance}")
                print('')
                return
        print("Error, Please Login")
        return
        
    def transfer(self, receiverID, amount):		
        if self.loginStatus == 1:
            if self.balance < amount:
                print(f"customer name     : {self.name}")
                print(f"your balance      : {self.balance}")
                print(f"transfer          : {amount}")
                print('transfer failed   : Not enough balance!')
                print('')
                return
            elif receiverID not in [data['ID'] for data in BankDB.accountDB]:
                print(f"customer name     : {self.name}")
                print(f"transfer to       : {receiverID}")
                print('transfer failed   : Target transfer not found!')
                print('')
                return
            for dataTarget in BankDB.accountDB:
                if dataTarget['ID'] == receiverID:
                    self.balance -= amount
                    BankDB.accountDB[self.index]['balance'] = self.balance
                    indexTarget = BankDB.accountDB.index(dataTarget)
                    BankDB.accountDB[indexTarget]['balance'] += amount
                    print(f"customer name     : {self.name}")
                    print(f"transaction time  : {datetime.datetime.now()}")
                    print(f"transfer to       : {dataTarget['name']}, {dataTarget['ID']}")
                    print(f"transfer (x_x)    : {amount}")
                    print(f"your balance now  : {self.balance}")
                    print('')
                    return
        print("Error, Please Login")
        return

    def logout(self):
        self.loginStatus = 0
        print("User Logout Successful")
        print('')
        return

        

BankDB('aria', '081374140707', 'pass123').register()
BankDB('budi', '081374140001', 'pass456').register()


aria = BankAccount('081374140707', 'pass123')
print(aria) 

budi = BankAccount('081374140001', 'pass456')
print(budi) 


aria.myBalance()
budi.myBalance()


aria.deposit(1000)
aria.withdraw(300)
aria.deposit(5000)
aria.withdraw(9000) # withdraw failed : Not enough balance!

aria.transfer('081374140001', 9000) # transfer failed : Not enough balance!
aria.transfer('081374140000', 5000) # transfer failed : Target transfer not found!
aria.transfer('081374140001', 5000)

aria.logout()


budi.myBalance()


aria = BankAccount('081374140707', 'pass333') # Wrong ID or Password
aria.deposit(1000) # Error, Please Login
aria.withdraw(300) # Error, Please Login

