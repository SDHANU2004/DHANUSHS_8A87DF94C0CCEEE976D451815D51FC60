class BankAccount:

    def __init__(self, account_number, account_holder_name, account_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.__account_balance = account_balance  
    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount > self.__account_balance:
            raise ValueError("Insufficient funds")
        self.__account_balance -= amount

    def get_balance(self):
        return self.__account_balance


def main():
    account = BankAccount("123456789", "Jeeva", 1000)

    account.deposit(500)
    print("Account balance:", account.get_balance())

    account.withdraw(200)
    print("Account balance:", account.get_balance())


if __name__ == "__main__":
    main()