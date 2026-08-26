class Transaction:

    def __init__(
        self,
        id,
        account_id,
        transaction_type,
        amount,
        balance_after,
        created_at
    ):
        self.id = id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after
        self.created_at = created_at