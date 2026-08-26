from datetime import datetime
from models.customer import Customer
from repositories.customer_repository import CustomerRepository

class CustomerService:

    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def register_customer(self, name, email, phone):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if not email.strip():
            raise ValueError("Email cannot be empty")
        if not phone.strip():
            raise ValueError("Phone cannot be empty")
        
        existing_customer = self.repository.get_by_email(email)

        if existing_customer is not None:
            raise ValueError("Email already registered")

        created_at = datetime.now().isoformat()

        customer = Customer(
            None,
            name,
            email,
            phone,
            created_at
        )

        customer_id = self.repository.create(customer)

        return customer_id