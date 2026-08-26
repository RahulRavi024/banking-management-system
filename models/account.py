class Account:

    def __init__(
        self,
        account_id,
        account_number,
        customer_id,
        account_type,
        balance,
        pin_hash,
        status,
        created_at
    ):
        self.account_id = account_id
        self.account_number = account_number
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance
        self.pin_hash = pin_hash
        self.status = status
        self.created_at = created_at