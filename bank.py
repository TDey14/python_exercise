

#bank app
'''create account
view account details by acc no
withdraw
deposit
fund transfer
print transaction
exit'''
#create bank class ,create methods,create collections to store for multiple accounts



class Bank:
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def create_account(self, acc_no, name, initial_balance=0):
        self.accounts[acc_no] = {"name": name, "balance": initial_balance}
        print(f"Account name: {name} account number {acc_no}")

    def view_account_details(self, acc_no):
        account = self.accounts.get(acc_no)
        if account:
            print(f"Account Number: {acc_no}")
            print(f"Name: {account['name']}")
            print(f"Balance: {account['balance']}")
        else:
            print("Account not found.")

    def deposit(self, acc_no, amount):
        account = self.accounts.get(acc_no)
        if account:
            account['balance'] += amount
            self.transactions.append(f"Deposit: {amount} to {acc_no}")
            print(f"Amount {amount} deposited to account {acc_no}")
        else:
            print("Account not found.")

    def withdraw(self, acc_no, amount):
        account = self.accounts.get(acc_no)
        if account:
            if account['balance'] >= amount:
                account['balance'] -= amount
                self.transactions.append(f"Withdrawal: {amount} from {acc_no}")
                print(f"Amount: {amount} withdrawn from: {acc_no}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def fund_transfer(self, from_acc_no, to_acc_no, amount):
        from_account = self.accounts.get(from_acc_no)
        to_account = self.accounts.get(to_acc_no)
        if from_account and to_account:
            if from_account['balance'] >= amount:
                from_account['balance'] -= amount
                to_account['balance'] += amount
                self.transactions.append(f"Transfer: {amount} from {from_acc_no} to {to_acc_no}")
                print(f"Amount {amount} from {from_acc_no} to {to_acc_no}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def print_transactions(self):
        print("Transactions:")
        for transaction in self.transactions:
            print(transaction)
    def get_account_data(self):
        acc_no = input("account number: ")
        name = input("account holder name: ")
        initial_balance = float(input("initial balance: "))
        return acc_no, name, initial_balance

    def get_deposit_data(self):
        acc_no = input("account number: ")
        amount = float(input("deposit: "))
        return acc_no, amount

    def get_withdrawal_data(self):
        acc_no = input("account number: ")
        amount = float(input("withdraw: "))
        return acc_no, amount

    def get_transfer_data(self):
        from_acc_no = input("source account number: ")
        to_acc_no = input("destination account number: ")
        amount = float(input("amount:"))
        return from_acc_no, to_acc_no, amount
    def run(self):
        while True:
            print("\nChoose an operation:")
            print("1. Create account")
            print("2. View account details")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Fund transfer")
            print("6. Print transactions")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                acc_no, name, initial_balance = self.get_account_data()
                self.create_account(acc_no, name, initial_balance)
            elif choice == '2':
                acc_no = input("Enter account number: ")
                self.view_account_details(acc_no)
            elif choice == '3':
                acc_no, amount = self.get_deposit_data()
                self.deposit(acc_no, amount)
            elif choice == '4':
                acc_no, amount = self.get_withdrawal_data()
                self.withdraw(acc_no, amount)
            elif choice == '5':
                from_acc_no, to_acc_no, amount = self.get_transfer_data()
                self.fund_transfer(from_acc_no, to_acc_no, amount)
            elif choice == '6':
                self.print_transactions()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice")


my_bank = Bank()
my_bank.run()

