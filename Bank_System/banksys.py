class Bank():
    
    def __init__ (self):
        x=False
        bank_data=[
    {
    'username':'Ahmed',
    'Password':2468,
    'Account_ballance':100000
    },
    {
    'username':'Mohamed',
    'Password':1234,
    'Account_ballance':200000
    },
    {
    'username':'Omar',
    'Password':5678,
    'Account_ballance':300000
    }
    ]
        self.number_of_accounts =len(bank_data)
        self.bank_data = bank_data
        self.x = x

    def user_register (self,newusername:str,newpassword:int)->None:
        a=False
        for i in range(len(self.bank_data)):
            if self.bank_data[i]['username']==newusername :
                print('This account is already registered Choose another user name')
                a=True
            else:
                break
        if a==False:
            self.newusername = newusername
            self.newpassword = newpassword
            self.account_ballance = 0
            self.number_of_accounts+=1
            print("Account created successfully!")
            self.bank_data.append({'username':self.newusername,'Password':self.newpassword,'Account_ballance':self.account_ballance})
            print( self.bank_data[self.number_of_accounts-1])
            


    def user_login (self,login_username:str,login_userpassword:int):
        for i in range(len(self.bank_data)):
            self.bank_data[i]['username']=(self.bank_data[i]['username']).lower()
        for i in range(len(self.bank_data)):
            if self.bank_data[i]['username']==login_username.lower() and self.bank_data[i]['Password']==login_userpassword:
                print(f'Login Successful! Welcome {self.bank_data[i]["username"]}')
                self.username = self.bank_data[i]['username']
                self.password = self.bank_data[i]['Password']
                self.account_ballance = self.bank_data[i]['Account_ballance']
                print(f'User name : {self.username}\nAccount ballance : {self.account_ballance}')
                self.x=True
                break
               
        if self.x==False:
            print(f"\nLogin Failed!\nUser name:'{login_username}' is not available to login")
            print("Please try again.\n")        


    def deposit (self,amount:float)->None:
        self.account_ballance += amount
        print(f'\nDeposit Successful! New account ballance: {self.account_ballance}')        

    def withdraw (self,amount:float)->None:
        if amount <= self.account_ballance:
            self.account_ballance -= amount
            print(f'\nWithdrawal Successful! New account ballance: {self.account_ballance}\n')
        else:
            print('\nInsufficient funds\n')
        
    
    def check_balance (self):
        print(f'Current account ballance: {self.account_ballance}\n')
        