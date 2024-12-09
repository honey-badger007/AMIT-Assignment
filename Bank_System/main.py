from banksys import Bank
import  time

bank=Bank()  

while True:
    print("Welcome to The Bank!")
    print("1. Create a new bank account")
    print("2. Login to your bank account")
    print("3. Exit")
    choice=input("Enter your choice: ")

    if choice=="1":
        print("Creating a new bank account...")
        username=input("Enter your user name: ")
        password=int(input("Enter your password: "))
        bank.user_register(username,password)
        time.sleep(5)

    elif choice=="2":
        print("Logging in...")
        username=input("Enter your user name: ")
        password=int(input("Enter your password: "))
        bank.user_login(username,password)
        while bank.x==True :
            print("1. Deposit money")
            print("2. Withdraw money")
            print("3. Check balance")
            print("4. Logout")
            choice2=input("Enter your choice: ")

            if choice2=="1":
                print("Depositing money...")
                amount=float(input("Enter the amount to deposit: "))
                bank.deposit(amount)

            elif choice2=="2":
                print("Withdrawing money...")
                amount=float(input("Enter the amount to withdraw: "))
                bank.withdraw(amount)
                
            elif choice2=="3":
                print("Checking balance...")
                bank.check_balance()
                
            elif choice2=="4":
                print("Logging out...")
                bank.x=False
                break
                
            else:
                print("Invalid choice. Please try again.\n")
        
        
    elif choice=="3":
        print("Thank you for using our Bank...\n")
        time.sleep(5)
        break
    else:
        print("Invalid choice. Please try again.\n")
        time.sleep(2)