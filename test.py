import unittest
from datetime import datetime
from code import Transaction, TransactionHistory, Account

# Test sprawdza czy obiekt Transaction działa poprawnie a dokładniej właściwości 'transaction_type' i 'amount' 
class TestTransaction(unittest.TestCase):
    def test_transaction_initialization(self):
        transaction = Transaction('deposit', 100, datetime.now())
        self.assertEqual(transaction.transaction_type, 'deposit')
        self.assertEqual(transaction.amount, 100)

class TestTransactionHistory(unittest.TestCase):

    # Test sprawdza czy dodawanie transakcji do historii działa
    def test_add_transaction(self):
        history = TransactionHistory()
        transaction = Transaction('deposit', 100, datetime.now())
        history.add_transaction(transaction)
        self.assertEqual(len(history.transactions), 1)

    # Test sprawdza czy metoda zwraca poprawnie transakcje z określonego zakresu
    def test_get_transactions_in_range(self):
        history = TransactionHistory()
        transaction1 = Transaction('deposit', 100, datetime(2023, 1, 1))
        transaction2 = Transaction('withdrawal', 50, datetime(2023, 1, 15))
        transaction3 = Transaction('deposit', 200, datetime(2022, 12, 30))
        transaction4 = Transaction('withdrawal', 15, datetime(2023, 2, 20))
        history.add_transaction(transaction1)
        history.add_transaction(transaction2)
        history.add_transaction(transaction3)
        history.add_transaction(transaction4)

        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 1, 31)
        transactions_info = history.get_transactions_in_range(start_date, end_date)
        
        self.assertEqual(len(transactions_info.split('\n')), 3)

class TestAccount(unittest.TestCase):

    # Test sprawdza czy inicjalizacja obiektu działa poprawnie
    def test_account_initialization(self):
        account = Account('12345', 500)
        self.assertEqual(account.account_number, '12345')
        self.assertEqual(account.balance, 500)
        Account.print_info(account)

    # Test sprawdza czy metoda deposit działa poprawnie
    def test_deposit(self):
        account = Account('12345', 500)
        account.deposit(100, datetime.now())
        self.assertEqual(account.balance, 600)

    # Test sprawdza czy metoda withdraw z dobrymi danymi działa poprawnie
    def test_withdraw(self):
        account = Account('12345', 500)
        account.withdraw(200, datetime.now())
        self.assertEqual(account.balance, 300)

    # Test sprawdza czy metoda withdraw ze złymi danymi działa poprawnie
    def test_insufficient_funds_withdraw(self):
        account = Account('12345', 100)
        account.withdraw(200, datetime.now())
        self.assertEqual(account.balance, 100)

    # Test sprawdza czy metoda withdraw z zerową wartością działa
    def test_zero_withdraw(self):
        account = Account('12345', 100)
        account.withdraw(0, datetime.now())
        self.assertEqual(account.balance, 100)

    # Test sprawdza czy metoda withdraw z ujemną wartością działa
    def test_negative_withdraw(self):
        account = Account('12345', 100)
        account.withdraw(-100, datetime.now())
        self.assertEqual(account.balance, 100)

    # Test sprawdza czy metoda transfer z dobrymi danymi działa poprawine
    def test_transfer(self):
        account1 = Account('12345', 500)
        account2 = Account('67890', 200)
        account1.transfer(account2, 100, datetime.now())
        self.assertEqual(account1.balance, 400)
        self.assertEqual(account2.balance, 300)

    # Test sprawdza czy metoda transfer ze złymi danymi działa poprawnie
    def test_insufficient_funds_transfer(self):
        account1 = Account('12345', 100)
        account2 = Account('67890', 200)
        account1.transfer(account2, 150, datetime.now())
        self.assertEqual(account1.balance, 100)
        self.assertEqual(account2.balance, 200)

    def test_zero_transfer(self):
        account1 = Account('12345', 100)
        account2 = Account('67890', 200)
        account1.transfer(account2, 0, datetime.now())
        self.assertEqual(account1.balance, 100)
        self.assertEqual(account2.balance, 200)

    def test_negative_transfer(self):
        account1 = Account('12345', 100)
        account2 = Account('67890', 200)
        account1.transfer(account2, -200, datetime.now())
        self.assertEqual(account1.balance, 100)
        self.assertEqual(account2.balance, 200)

if __name__ == '__main__':
    unittest.main()
