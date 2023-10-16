class User:

    acc_no = 0

    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.loan_taken = 0


    def generate_account_number(self):
        User.acc_no += 1
        return User.acc_no
        
    def deposit_bal(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit bal: {amount}")
        else: 
            print("Sorry wrong input :(")

    def withdraw_bal(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawal bal: {amount}")
            else:
                print("Withdrawal amount exceeded and cause bankruptcy :((")
        else:
            print("Sorry wrong input :(")

    def check_bal(self):
        return self.balance

    def check_transaction_history(self):
        for ele in self.transaction_history:
            print(ele)

    
    def take_loan(self, amount):
        if self.loan_taken < 2:
            if amount > 0:
                self.loan_taken += 1
                self.balance += amount
                self.transaction_history.append(f"loan amount: {amount}")
            else:
                print("Sorry wrong input :(")

        else:
            print("Already taken max times! :)") 

    
    def trasfer_amount(self, recipient, amount):
        if amount > 0 and self.balance >= amount:
            if recipient:
                self.balance -= amount
                recipient.deposit(amount)
                self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
                print(f"transfer done {amount}")

            else:
                print("Account does not exist.")
        else:
            print("Sorry wrong input :(")


class Admin:
    def __init__(self):
        self.user_accounts = []
        self.loan_feature_enabled = True


    def create_user_account(self, user):
        self.user_accounts.append(user)
        print(f"account created successfully!")
    
    def delete_user_account(self, user_name):
        for user in self.user_accounts:
            if user.name == user_name:
                self.user_accounts.remove(user)
                print(f"Deleted user account!")
                return 
        print(f"User account not found.")


    def see_all_acc(self):
        for user in self.user_accounts:
            print(f"Name: {user.name}, Email: {user.email}, Account type: {user.account_type}")
    
    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.user_accounts)
        return total_balance

    def check_total_loan(self):
        total_loan_amount = sum(user.balance for user in self.user_accounts)
        return total_loan_amount


    def control_loan_feature(self):
        if self.loan_feature_enabled:
            self.loan_feature_enabled = False
            print("Loan feature is now off")
        else:
            self.loan_feature_enabled = True
            print("Loan feature is now on")


admin = Admin()

while True:
    print("\nOptions:")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Exit")

    choice = input("Enter your choice for bank management software: ")


    if choice == "1":

        name = input("Enter your name please: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter your account type (Savings or Current): ")
        user = User(name, email, address, account_type)
        admin.create_user_account(user)

        print("Account created successful.")

        while True:
            print("\n User Options:")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Take a Loan")
            print("4. Transfer Money")
            print("5. Check Balance")
            print("6. View Transaction History")
            print("7. Exit to Main Menu")

            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                user.deposit_bal(amount)

            elif user_choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                user.withdraw_bal(amount)

            elif user_choice == "3":
                amount = float(input("Enter the loan amount: "))
                user.take_loan(amount)

            elif user_choice == "4":
                recipient_name = input("Enter recipient's name: ")
                recipient = None

                for i in admin.user_accounts:
                    if i.name == recipient_name:
                        recipient = i
                        break
                if recipient:
                    amount = float(input("Enter the amount to transfer: "))
                    user.trasfer_amount(recipient, amount)
                else:
                    print("account no exist sry!")

            elif user_choice == "5":
                print(f"Available Balance: {user.check_bal()}")

            elif user_choice == "6":
                user.check_transaction_history()

            elif user_choice == "7":
                break

    elif choice == "2":
        print("\nAdmin Login: ")
        print("1. Delete user accounts")
        print("2. See all user accounts")
        print("3. Check total balance")
        print("4. Check total loan amount")
        print("5. Toggle loan feature")
        print("6. Back to main menu")

        admin_choice = input("Enter your choice: ")

        if admin_choice == "1":
            print("\nUser Accounts:")
            admin.see_all_acc()
            user_name = input("enter the name want to delete: ")
            admin.delete_user_account(user_name)

        elif admin_choice == "2":
            print("\nUser Accounts:")
            admin.see_all_acc()

        elif admin_choice == "3":
            total_balance = admin.check_total_balance()
            print(f"Total Balance: {total_balance}")
        
        elif admin_choice == "4":
            total_loan = admin.check_total_loan()
            print(f"Total loan: {total_loan}")
            

        elif admin_choice == "5":
            admin.control_loan_feature()
            print("Loan feature moved!")

        elif admin_choice == "6":
            continue

    elif choice == "3":
        break
        






































