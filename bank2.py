class BankAccount:
    def __init__(self, account_number, password, balance=0):
        self.account_number = account_number
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount}. New balance: ${self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


def create_account(accounts):
    account_number = input("Enter new account number: ")
    if account_number in accounts:
        print("Account number already exists. Try again.")
        return

    password = input("Enter new password: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    accounts[account_number] = BankAccount(account_number, password, initial_deposit)
    print(f"Account created successfully for account number {account_number}.")


def login(accounts):
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")
    account = accounts.get(account_number)

    if account and account.password == password:
        print("Login successful.")
        return account
    else:
        print("Login failed. Invalid account number or password.")
        return None


def main():
    accounts = {}

    while True:
        print("\nWelcome to the Bank!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            account = login(accounts)
            if account:
                while True:
                    print("\n1. Deposit Amount")
                    print("2. Withdraw Amount")
                    print("3. Logout")
                    option = input("Choose an option: ")

                    if option == '1':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif option == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif option == '3':
                        print("Logging out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting. Thank you for using the bank!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
