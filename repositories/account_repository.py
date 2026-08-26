from models.account import Account
import hashlib

class AccountRepository:

    def __init__(self, connection):
        self.connection = connection

    def create(self, account):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO accounts
            (account_number, customer_id, account_type, balance, pin_hash, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            account.account_number,
            account.customer_id,
            account.account_type,
            account.balance,
            account.pin_hash,
            account.status,
            account.created_at
        ))
        self.connection.commit()
        return cursor.lastrowid
    
    def get_by_account_number(self, account_number):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM accounts
            WHERE account_number = ?
        """, (account_number,))
        row = cursor.fetchone()
        if row is None:
            return None
        return Account(*row)
        
        
    def get_by_id(self, account_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM accounts
            WHERE account_id = ?
        """, (account_id,))
        row = cursor.fetchone()
        if row is None:
            return None
        return Account(*row)


    def update_balance(self, account_id, new_balance):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE accounts
            SET balance = ?
            WHERE account_id = ?
        """, (new_balance, account_id))
        self.connection.commit()
        
    def update_pin_hash(self, account_id, new_pin_hash):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE accounts
            SET pin_hash = ?
            WHERE account_id = ?
        """, (new_pin_hash, account_id))
        self.connection.commit()
        
    def close_account(self, account_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE accounts
            SET status = ?
            WHERE account_id = ?
        """, ("CLOSED", account_id))
        self.connection.commit()