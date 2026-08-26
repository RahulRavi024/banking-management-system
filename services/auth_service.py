import hashlib

class AuthService:
    def __init__(self, repository):
        self.repository = repository
    
    def login(self, account_number, pin):
        pin_hash = hashlib.sha256(pin.encode()).hexdigest()
        account = self.repository.get_by_account_number(account_number)
        if account is None:
            raise ValueError("Account not found")
        if account.pin_hash != pin_hash:
            raise ValueError("Invalid PIN")
        if account.status != "ACTIVE":
            raise ValueError("Account is not active")
        return account
    
    def change_pin(self, account_id, old_pin, new_pin):
        if len(new_pin) != 4 or not new_pin.isdigit():
            raise ValueError("PIN must be exactly 4 digits")
        account = self.repository.get_by_id(account_id)
        if account is None:
            raise ValueError("Account not found")
        old_pin_hash = hashlib.sha256(old_pin.encode()).hexdigest()
        if account.pin_hash != old_pin_hash:
            raise ValueError("Current PIN is incorrect")
        new_pin_hash = hashlib.sha256(new_pin.encode()).hexdigest()
        self.repository.update_pin_hash(
            account_id,
            new_pin_hash
        )