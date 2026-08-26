from datetime import datetime

from models.transaction import Transaction
from repositories.account_repository import AccountRepository
from repositories.transaction_repository import TransactionRepository

class TransactionService:

    def __init__(self, transaction_repository, account_repository):
        self.transaction_repository = transaction_repository
        self.account_repository = account_repository

    def deposit(self, account_id, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        account = self.account_repository.get_by_id(account_id)
        if account is None:
            raise ValueError("Account not found")
        new_balance = account.balance + amount
        self.account_repository.update_balance(
            account_id,
            new_balance
        )
        transaction = Transaction(
            None,
            account_id,
            "DEPOSIT",
            amount,
            new_balance,
            datetime.now().isoformat()
        )
        self.transaction_repository.create(transaction)
        return transaction

    def withdraw(self, account_id, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        account = self.account_repository.get_by_id(account_id)
        if account is None:
            raise ValueError("Account not found")
        if amount > account.balance:
            raise ValueError("Insufficient balance")
        new_balance = account.balance - amount
        self.account_repository.update_balance(
            account_id,
            new_balance
        )
        transaction = Transaction(
            None,
            account_id,
            "WITHDRAW",
            amount,
            new_balance,
            datetime.now().isoformat()
        )
        self.transaction_repository.create(transaction)
        return transaction

    def transfer(self, sender_account_id, receiver_account_number, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than 0")
        sender = self.account_repository.get_by_id(sender_account_id)
        if sender is None:
            raise ValueError("Sender account not found")
        receiver = self.account_repository.get_by_account_number(receiver_account_number)
        if receiver is None:
            raise ValueError("Receiver account not found")
        if sender.account_id == receiver.account_id:
            raise ValueError("Cannot transfer money to the same account")
        if amount > sender.balance:
            raise ValueError("Insufficient balance")
        sender_new_balance = sender.balance - amount
        receiver_new_balance = receiver.balance + amount
        self.account_repository.update_balance(sender.account_id, sender_new_balance)
        self.account_repository.update_balance(receiver.account_id, receiver_new_balance)
        sender_transaction = Transaction(
            None,
            sender.account_id,
            "TRANSFER_OUT",
            amount,
            sender_new_balance,
            datetime.now().isoformat()
        )
        self.transaction_repository.create(sender_transaction)
        receiver_transaction = Transaction(
            None,
            receiver.account_id,
            "TRANSFER_IN",
            amount,
            receiver_new_balance,
            datetime.now().isoformat()
        )
        self.transaction_repository.create(receiver_transaction)
        return sender_transaction

    def get_history(self, account_id):
        return self.transaction_repository.get_by_account_id(account_id)