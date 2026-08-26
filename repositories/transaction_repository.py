from models.transaction import Transaction


class TransactionRepository:

    def __init__(self, connection):
        self.connection = connection

    def create(self, transaction):
        cursor = self.connection.cursor()

        cursor.execute("""
            INSERT INTO transactions
            (account_id, transaction_type, amount, balance_after, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            transaction.account_id,
            transaction.transaction_type,
            transaction.amount,
            transaction.balance_after,
            transaction.created_at
        ))

        self.connection.commit()

        return cursor.lastrowid

    def get_by_account_id(self, account_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM transactions
            WHERE account_id = ?
            ORDER BY created_at DESC
        """, (account_id,))
        rows = cursor.fetchall()
        transactions = []
        for row in rows:
            transaction = Transaction(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )
            transactions.append(transaction)
        return transactions