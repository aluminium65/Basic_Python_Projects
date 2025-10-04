
class BankAcc:
    Acc_list = {}
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        BankAcc.Acc_list[self.name] = self
        
    
    def deposit(self):
        print("\nEnter the amount you want to deposit:")
        
        while True:
            try:
                amount = input("  >> ")
                amount = float(amount)
            except ValueError:
                print("The amount must be in numbers!")
            if amount < 0:
                print("Negative amounts are not supported.")
            else:
                break
        
        self.balance += amount
        print(f"[*] The amount:{amount} successfully added to your account.")

    
    def withdraw(self):
        print("\nEnter the amount you want to withdraw:")

        while True:
            try:
                amount = input("  >> ")
                amount = float(amount)
            except ValueError:
                print("The amount must be in numbers!")
            if amount < 0:
                print("Negative amounts are not supported.")
            elif amount > self.balance:
                print("Insufficient balance!")
            else:
                break

        self.balance -= amount
        print(f"[*] The amount:{amount} successfully deducted from your account.")

    
    def display_balance(self):
        print(f"\n\tAccount Name: {self.name}\n\tCurrent Balance:{self.balance}$.")


print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++
+                                                  +
+             Aluminium Banking System             +
+                                                  +
++++++++++++++++++++++++++++++++++++++++++++++++++++
\n''')
print("\nWelcome to Aluminium Banking Inc.")
print("\n[GITHUB] https://github.com/aluminium65/")

while True:
    
    while True:
        print("\nSelect the desired option from the menu:")
        print('''
1, Create An account
2, Check Balance
3, Deposit
4, Withdraw
5, Exit
''')
    
        try:
            option = input("  >> ")
            option = int(option)
            break
        except ValueError:
            print("The option must be a number.")
    
    
    if option == 1:
        print("Enter your full name:")
        full_name = input("  >> ")
        
        if full_name in BankAcc.Acc_list.keys():
            print("[*] This name is already in use.")
        else:
            full_name = BankAcc(full_name)
            print('\n[*] Account successfully created')
            full_name.display_balance()


    elif option == 2:
        print("Enter Your full name:")
        full_name = input("  >> ")
        
        if full_name in BankAcc.Acc_list.keys():
            BankAcc.Acc_list[full_name].display_balance()
        else:
            print("No match found!")
            
    
    elif option == 3:
        print("Enter Your full name:")
        full_name = input("  >> ")
        
        if full_name in BankAcc.Acc_list.keys():
            print("\nFound a match!")
            BankAcc.Acc_list[full_name].deposit()
    
        else:
            print("\nNo match found!")
    

    elif option == 4:
        print("Enter the full name:")
        full_name = input("  >> ")

        if full_name in BankAcc.Acc_list.keys():
            print("\nFound a match!")
            BankAcc.Acc_list[full_name].withdraw()
        else:
            print("\nNo match found!")

    
    elif option == 5:
        print("Have a good day!")
        break
    
    
    else:
        print("Invalid option")
