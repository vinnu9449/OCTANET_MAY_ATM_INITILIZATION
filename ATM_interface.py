class ATM:
    def _init_(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def display_menu(self):
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def transactions_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: ${amount}")
        print("Deposit successful.")

    def transfer(self, amount, recipient_id):
        # Logic for transferring funds to another account
        pass

# Sample usage:
def main():
    user_id = input("Enter user ID: ")
    pin = input("Enter PIN: ")

    atm = ATM(user_id, pin)

    while True:
        atm.display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            atm.transactions_history()
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == "3":
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        elif choice == "4":
            amount = float(input("Enter transfer amount: "))
            recipient_id = input("Enter recipient's user ID: ")
            atm.transfer(amount, recipient_id)
        elif choice == "5":
            print("Thank you for using our ATM.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()