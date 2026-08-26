from models.account import Account
from datetime import datetime
import hashlib
import random
class AccountService:
    def __init__(self, repository):
        self.repository = repository
    def create_account(self, customer_id, account_type, pin):
        if len(pin) != 4 or not pin.isdigit():
            raise ValueError("PIN must be a 4-digit number")
        pin_hash = hashlib.sha256(pin.encode()).hexdigest()
        account_number = str(random.randint(100000, 999999))
        created_at = datetime.now().isoformat()
        account = Account(
            None,
            account_number,
            customer_id,
            account_type,
            0.0,
            pin_hash,
            "ACTIVE",
            created_at
        )
        account_id = self.repository.create(account)
        return account
    def close_account(self, account_id):
        account = self.repository.get_by_id(account_id)
        if account is None:
            raise ValueError("Account not found")
        if account.status == "CLOSED":
            raise ValueError("Account is already closed")
        self.repository.close_account(account_id)