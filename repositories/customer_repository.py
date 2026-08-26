from models.customer import Customer


class CustomerRepository:

    def __init__(self, connection):
        self.connection = connection

    def create(self, customer):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO customers
            (name, email, phone, created_at)
            VALUES (?, ?, ?, ?)
        """, (
            customer.name,
            customer.email,
            customer.phone,
            customer.created_at
        ))
        self.connection.commit()
        return cursor.lastrowid

    def get_by_id(self, customer_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT
                customer_id,
                name,
                email,
                phone,
                created_at
            FROM customers
            WHERE customer_id = ?
        """, (customer_id,))
        row = cursor.fetchone()
        if row is None:
            return None
        return Customer(*row)

    def get_by_email(self, email):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT
                customer_id,
                name,
                email,
                phone,
                created_at
            FROM customers
            WHERE email = ?
        """, (email,))
        row = cursor.fetchone()
        if row is None:
            return None
        return Customer(*row)