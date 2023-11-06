#CityBank ATM machine:
import random
import pickle
import datetime
import pprint


class CityBank:
    def __init__(self,name,amount,account_num,transactions):
        self.name = name
        self.amount = amount
        self.account_num = account_num
        self.x = {'name': self.name, 'account_type': 'Checking', 'current_balance': amount, 'account_number': self.account_num, 'transactions': transactions}        
        self.y = {}
        self.deposit = 0
        self.withdrawal = 0
        
    def create_account(self):
        #user creates a new bank account with his/her name and deposits some money:
        self.x = {'name': self.name, 'account_type': 'Checking', 'current_balance': self.amount, 'account_number': self.account_num, 'transactions': [] }
        self.open_new_user_file()
        
    def user_info(self,account_data):
        print("\n\n")
        pprint.pprint(account_data)
        print("\n\n")
      

    def open_new_user_file(self):
        #store new user info in a pkl file for future reference:
        with open(f"C:\\Users\\aksha\\{self.account_num}.pkl","wb") as file:
            pickle.dump(self.x, file)

    def open_return_user_file(self):
        with open(f"C:\\Users\\aksha\\{self.account_num}.pkl","wb") as file:
            pickle.dump(self.x, file)

    def create_savings(self):
        self.withdrawal_amount(self.x,"checking")  
        self.y = {'name': self.name, 'account_type': 'Savings', 'current_balance': self.withdrawal, 'account_number': self.account_num, 'transactions': []}                     
        with open(f"C:\\Users\\aksha\\{self.account_num}_saving.pkl","wb") as file:
            pickle.dump(self.y,file)
    
    def open_return_user_savings(self):
        with open(f"C:\\Users\\aksha\\{self.account_num}_saving.pkl","wb") as file:
            pickle.dump(self.y,file)
    

    def deposit_amount(self,account_data,account_type):
        #self.deposit is needed later in the print statement to print it out.
        account_data['transactions'].append({"transaction_time":f"{datetime.datetime.now()}","deposit": f"{self.deposit}"})
        account_data['current_balance'] += self.deposit
        if account_type == "checking":
            self.open_return_user_file()
        elif account_type == "savings":
            self.open_return_user_savings()
            
        print(f"\nAmount {self.deposit} was deposited, current {account_type} balance: {account_data['current_balance']}") 
        
    def withdrawal_amount(self,account_data,account_type):
        #self.withdrawal is needed in the print statement to print it out.
        account_data["transactions"].append({"transaction_time":f"{datetime.datetime.now()}","withdrawal": f"{self.withdrawal}"})
        account_data['current_balance'] -= self.withdrawal
        if account_type == "checking":
            self.open_return_user_file()
        elif account_type == "savings":
            self.open_return_user_savings()   
        print(f"\nAmount {self.withdrawal} withdrawn, current {account_type} balance: {account_data['current_balance']}")

    def know_balance(self):
        print(f"\nThe current balance is:{self.x['current_balance']}")
      
        
