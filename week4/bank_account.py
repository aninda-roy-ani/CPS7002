
class BankAccount:
    bank_name = "Barclays"
    next_account_id = 1

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.id = self.next_account_id
        self.balance = balance
        self.next_account_id += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited £{amount}. New balance: £{self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew £{amount}. New balance: £{self.balance}.")
        else:
            print("Insufficient funds")

    def display_info(self):
        print(f"{self.bank_name} | ID: {self.id}, Balance: £{self.balance} | Holder: {self.account_holder}.")


if __name__ == "__main__":
    # Creating instances of the BankAccount class.
    alice_account = BankAccount(account_holder="Alice Khan", balance=1000)
    bob_account = BankAccount(account_holder="Bob Smith", balance=500)

    # Modifying instance attribute.
    alice_account.withdraw(200)
    bob_account.deposit(200)

    # Modifying class attribute (affects all instances).
    BankAccount.bank_name = "ABC Bank"

    # Displaying updated information.
    alice_account.display_info()
    bob_account.display_info()