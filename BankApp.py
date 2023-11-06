from Brijesh_day16_classbank import CityBank
import pickle
import random
import pprint
import datetime
sep_line = '-'*140
print("Hi! welcome to city bank!:")
print('''                                                                                   
  ,ad8888ba,  88                     88888888ba                         88         
 d8"'    `"8b ""   ,d                88      "8b                        88         
d8'                88                88      ,8P                        88         
88            88 MM88MMM 8b       d8 88aaaaaa8P' ,adPPYYba, 8b,dPPYba,  88   ,d8   
88            88   88    `8b     d8' 88""""""8b, ""     `Y8 88P'   `"8a 88 ,a8"    
Y8,           88   88     `8b   d8'  88      `8b ,adPPPPP88 88       88 8888[           
 Y8a.    .a8P 88   88,     `8b,d8'   88      a8P 88,    ,88 88       88 88`"Yba,   
  `"Y8888Y"'  88   "Y888     Y88'    88888888P"  `"8bbdP"Y8 88       88 88   `Y8a  
                             d8'                                                   
                            d8'

    
 
          __  __                                             
         |. ||. |    .|                                      
         || ||| |    | |                W                    
         |: ||: |    |'|               [ ]         ._____    
         |  ||  |   |  |     .--'|      3   .---"| |.   |'   
     _   |  ||  |-. |  | __  |.  |     /|  _|__  | ||   |__  
  .-'|  _|  ||  | ||   '-  | ||    \|// / |   |' | |    | |' 
  |' | |.|  ||  | ||       '-'    -( )-|  |   |  | |    | |  
__|  '-' '  ''  ' ""       '       J V |  `   -  |_'    ' |__
                             ___  '    /                     
                             \  \/    |          ''')

bank_open = True

while bank_open == True:
    def user_in():
        success = False
        while not success:
                user_input_1 = input('''\n If you are a returning user press 1,
                if you are our new customer press 2 to create an account,
                if you want to quit press 'q':''')
                success = (user_input_1 in ['1','2','q'])
        return user_input_1               
    user_input_1 = user_in()        
    if  user_input_1 == 'q':
        print()
        print("\nGood bye!")
        print('''                                                                                  
  ,ad8888ba,  88                     88888888ba                         88         
 d8"'    `"8b ""   ,d                88      "8b                        88         
d8'                88                88      ,8P                        88         
88            88 MM88MMM 8b       d8 88aaaaaa8P' ,adPPYYba, 8b,dPPYba,  88   ,d8   
88            88   88    `8b     d8' 88""""""8b, ""     `Y8 88P'   `"8a 88 ,a8"    
Y8,           88   88     `8b   d8'  88      `8b ,adPPPPP88 88       88 8888[      
 Y8a.    .a8P 88   88,     `8b,d8'   88      a8P 88,    ,88 88       88 88`"Yba,   
  `"Y8888Y"'  88   "Y888     Y88'    88888888P"  `"8bbdP"Y8 88       88 88   `Y8a  
                             d8'                                                   
                            d8'                                                    

''')
        bank_open = False

        
# For returning user press 1:



    elif int(user_input_1) == 1:
        
        
# Here the code opens the pkl file for a returning user from the directory:
        def create_return_obj():
            success = False
            while not success:
                
                try:
                    print(sep_line)
                    account = int(input("\nPlease enter your 4 digit account number to access your account:"))
                    print("\n")
                    with open(f"C:\\Users\\aksha\\{account}.pkl","rb") as user_file:
                         user_info = pickle.load(user_file)
                         ret_user_obj = CityBank(user_info['name'],user_info['current_balance'],user_info['account_number'],user_info['transactions'])
                    success = True
                except ValueError:
                    print(sep_line)
                    print("\nInvalid input! please try again!")
                except FileNotFoundError:
                    print(sep_line)
                    print("\nIncorrect pin! please try again!")
            return ret_user_obj           

        user_done = False
        return_user = create_return_obj()
        
# This is to let the user navigate through the Citybank menu options:
         
  
        while not user_done:
            success = False
            while not success:
                try:
                    print(sep_line)
                    user_input = int(input('''\nWhat would you like to do today?:\n Press 1 for deposit,\n Press 2 for withdrawal,
                           \n Press 3 for balance enquiry, \n Press 4 for user info, \n Press 5 to create your savings account, \n Press 6 to access your savings account \n Press 0 to exit'''))
                    success = (user_input in [1,2,3,4,5,6,0])
                except ValueError:
                    print(sep_line)
                    print("\n\nInvalid input! please try again!")
                
                
            if user_input == 1:
                print(sep_line)
                return_user.deposit =  float(input("\nEnter the amount you want to deposit:"))
                return_user.deposit_amount(return_user.x,"checking")
            elif user_input == 2:
                print(sep_line)
                return_user.withdrawal =  float(input("\nEnter the amount you want to withdraw:"))  
                return_user.withdrawal_amount(return_user.x,"checking")
            elif user_input == 3:
                print(sep_line)
                return_user.know_balance()
            elif user_input == 4:
                print(sep_line)
                return_user.user_info(return_user.x)
                
#This is for savings account creation( Creates a new pkl file and updates to self.y in the object return_user. ):

                
            elif user_input == 5:
                print(sep_line)
                print("\nHi! welcome to CityBank savings account creation!")
                print("..please note that you need to deposit a minimum of 100$\n to create your svaings account")
                print("\n")
                success = False
                while not success:
                    print(sep_line)
                    user_savings_input = input("would you like to transfer amount from your Checking account?: \n 'y' or 'n'").lower()
                    success = (user_savings_input in ['y','n'])
                if user_savings_input == 'y':
                    print(sep_line)
                    return_user.withdrawal =  float(input("\nEnter the amount you want to withdraw:"))
                    if return_user.withdrawal >= 100:
                         return_user.create_savings()
                         print("\nYour savings account is ready!! \n You can access the account by logging in to you CityBank account!")
                    else:
                        print(sep_line)
                        print("\nSorry you need to deposit 100$ to create a savings account!")
                elif user_savings_input == 'n':
                    print(sep_line)
                    print("\nNo problem! you can create a savings account at any time!")
                        
                else:
                    print(sep_line)
                    print("\nInvalid input! please try again!")

#This is for getting into the savings account( opens the pkl file and modifies the content and dumps it back )
                    
            elif user_input == 6:
                try:
                    with open(f"C:\\Users\\aksha\\{return_user.account_num}_saving.pkl","rb") as file:
                            return_user.y = pickle.load(file)
                            print(sep_line)
                            print("\n You are in your savings account!")
                    success = False
                    while not success:
                        try:
                            print(sep_line)
                            user_saving_trans = int(input("\nWould you like to do?:\n 1. Deposit \n 2. Withdraw \n 3. Savings account info"))
                            success = (user_saving_trans in [1,2,3])
                        except ValueError:
                            print(sep_line)
                            print("\n\nInvalid input! please try again!")
                        
                        
                    if user_saving_trans == 1:
                            print(sep_line)
                            user_savings_depo = input("\nWould you like to transfer the amount from your Checking account?: 'y' or 'n':").lower()
                            if user_savings_depo == 'y':
                                print(sep_line)
                                return_user.withdrawal =  float(input("\nEnter the amount you want to withdraw:"))  
                                return_user.withdrawal_amount(return_user.x,"checking")
                                return_user.y["current_balance"] += return_user.withdrawal
                               
                                return_user.y["transactions"].append({"transaction_time":f"{datetime.datetime.now()}","deposit": f"{return_user.withdrawal}"})
                                return_user.open_return_user_savings()
                                print(sep_line)
                                print(f"\nAmount {return_user.withdrawal} was deposited, current savings account balance: {return_user.y['current_balance']}") 

                            elif user_savings_depo == "n":
                                print(sep_line)
                                return_user.deposit =  float(input("\nEnter the amount you want to deposit:"))  
                                return_user.deposit_amount(return_user.y,"savings")
                                                                                           
                    elif user_saving_trans == 2:
                            print(sep_line)
                            return_user.withdrawal =  float(input("\nEnter the amount you want to withdraw:"))  
                            return_user.withdrawal_amount(return_user.y,"savings")
                            
                    elif user_saving_trans == 3:
                            return_user.user_info(return_user.y)
                            
                    
                          
                            
                except FileNotFoundError:
                    print(sep_line)
                    print("\nSorry! you do not have a savings account yet. \n please create a savings account to access this service. Thank you!")

                
            elif user_input == 0:
                    user_done = True
                    print(sep_line)
                    print("\nHave a nice day!")
                
#Press 2 for new user account creation:        
    elif int(user_input_1) == 2:
        print("\n\n")
        print(sep_line)
        print("Welcome to CityBank account creation!!")
        print(".....We will need some of your personal info..")
        print("...This won't take long..thank you for your patience!")
        new_password = random.randint(1000,1999)
        print("\n")
        print(sep_line)
        new_user = CityBank(input("Please enter your full name for the record"), float(input("\nPlease enter the amount you want to deposit!")), new_password, [])
        new_user.create_account()
        print(sep_line)
        print(f"\nThank you, we have created a new Checking account for you!!,\n your account number is: {new_password} \n please remember your account number for future transactions with us! Thank you")
        
  
    else:
       print(sep_line)
       print("\nInvalid input!! please try again!")
