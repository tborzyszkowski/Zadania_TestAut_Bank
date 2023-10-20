from datetime import datetime


class Account:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = TransactionHistory()

    def deposit(self, amount, timestamp):
        self.balance += amount
        transaction = Transaction('deposit', amount, timestamp)
        self.transaction_history.add_transaction(transaction)

    def withdraw(self, amount, timestamp):
        if amount < 0:
            print("Zła kwota")
        elif amount == 0:
            print("Operacja nie ma sensu")
        elif self.balance >= amount:
            self.balance -= amount
            transaction = Transaction('withdrawal', amount, timestamp)
            self.transaction_history.add_transaction(transaction)
        else:
            print("Niewystarczające środki!")

    def transfer(self, target_account, amount, timestamp):
        if amount < 0:
            print("Zła kwota")
        elif amount == 0:
            print("Operacja nie ma sensu")
        elif self.balance >= amount:
            self.balance -= amount
            transaction = Transaction('transfer', amount, timestamp)
            self.transaction_history.add_transaction(transaction)
            target_account.deposit(amount, timestamp)
        else:
            print("Niewystarczające środki!")
    
    def print_info(self):
        number = self.account_number
        balance = self.balance

        print(f"Numer Konta - {number} \nBalans - {balance}")
        

class Transaction:
    def __init__(self, transaction_type, amount, timestamp):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp

class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions_in_range(self, start_date, end_date):
        filtered_transactions = [transaction for transaction in self.transactions
                                 if start_date <= transaction.timestamp <= end_date]
        
        transactions_info = ""
        for transaction in filtered_transactions:
            transactions_info += (f"Typ: {transaction.transaction_type}, Ilość: {transaction.amount}, "
                                  f"Data: {transaction.timestamp}\n")
            print(f"Typ: {transaction.transaction_type}, Ilość: {transaction.amount}, "
                  f"Data: {transaction.timestamp}")
        
        return transactions_info
