from database.db import get_connection
from database.schema import create_tables
from repositories.customer_repository import CustomerRepository
from repositories.transaction_repository import TransactionRepository
from services.customer_service import CustomerService
from services.auth_service import AuthService
from repositories.account_repository import AccountRepository
from services.account_service import AccountService
from services.transaction_service import TransactionService


def show_main_menu():
    print("\n=================================")
    print("      BANKING MANAGEMENT SYSTEM")
    print("=================================")
    print("1. Register")
    print("2. Login")
    print("3. Exit")


def show_account_menu():
    print("\n=================================")
    print("          ACCOUNT MENU")
    print("=================================")
    print("1. View Profile")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Transaction History")
    print("7. Change PIN")
    print("8. Close Account")
    print("9. Logout")


def register(customer_service):
    print("\n--- Customer Registration ---")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")

    try:
        customer_id = customer_service.register_customer(name, email, phone)
        print("Customer registered successfully!")
        print(f"Customer ID: {customer_id}")
        return customer_id
    except ValueError as error:
        print(f"Registration failed: {error}")


def login(auth_service, transaction_service, account_service):
    print("\n--- Login ---")
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    try:
        account = auth_service.login(account_number, pin)
        print("\nLogin successful!")
        print(f"Welcome! Account Number: {account.account_number}")
        account_menu(account, transaction_service, auth_service, account_service)
    except ValueError as e:
        print(e)

def account_menu(account, transaction_service, auth_service, account_service):

    while True:
        show_account_menu()

        choice = input("Enter your choice: ")

        try:
            # 1. View Profile
            if choice == "1":
                print("\n===== PROFILE =====")
                print(f"Account ID: {account.account_id}")
                print(f"Account Number: {account.account_number}")
                print(f"Customer ID: {account.customer_id}")
                print(f"Account Type: {account.account_type}")
                print(f"Balance: {account.balance}")
                print(f"Created At: {account.created_at}")

            # 2. Check Balance
            elif choice == "2":
                print("\n===== BALANCE =====")
                print(f"Current Balance: {account.balance}")

            # 3. Deposit
            elif choice == "3":
                amount = float(input("Enter deposit amount: "))

                transaction = transaction_service.deposit(
                    account.account_id,
                    amount
                )

                account.balance = transaction.balance_after

                print("Deposit successful!")
                print(f"New Balance: {account.balance}")

            # 4. Withdraw
            elif choice == "4":
                amount = float(input("Enter withdrawal amount: "))

                transaction = transaction_service.withdraw(
                    account.account_id,
                    amount
                )

                account.balance = transaction.balance_after
                print("Withdrawal successful!")
                print(f"New Balance: {account.balance}")

            # 5. Transfer
            elif choice == "5":
                receiver_account_number = input("Enter receiver account number: ")
                amount = float(input("Enter transfer amount: "))
                transaction = transaction_service.transfer(
                    account.account_id,
                    receiver_account_number,
                    amount
                )
                account.balance = transaction.balance_after
                print("Transfer successful!")
                print(f"New Balance: {account.balance}")

            # 6. Transaction History
            elif choice == "6":
                transactions = transaction_service.get_history(account.account_id)
                print("\n===== TRANSACTION HISTORY =====")
                if not transactions:
                    print("No transactions found.")
                else:
                    for transaction in transactions:
                        print(
                            f"{transaction.transaction_type} | "
                            f"Amount: {transaction.amount} | "
                            f"Balance After: {transaction.balance_after} | "
                            f"{transaction.created_at}"
                        )

            # 7. Change PIN
            elif choice == "7":
                old_pin = input("Enter current PIN: ")
                new_pin = input("Enter new 4-digit PIN: ")
                confirm_pin = input("Confirm new PIN: ")
                if new_pin != confirm_pin:
                    raise ValueError("New PINs do not match")
                auth_service.change_pin(
                    account.account_id,
                    old_pin,
                    new_pin
                )
                print("PIN changed successfully!")

            # 8. Close Account
            elif choice == "8":
                confirmation = input("Are you sure you want to close your account? (y/n): ")
                if confirmation.lower() == "y":
                    account_service.close_account(account.account_id)
                    print("Account closed successfully.")
                    break
                else:
                    print("Account closure canceled.")
            
            #9. Logout
            elif choice == "9":
                print("Logging out...")
                break

            else:
                print("Invalid choice.")

        except ValueError as e:
            print(f"Error: {e}")

def create_account(customer_id, account_service):
    print("\n--- Create Account ---")
    print("1. Savings Account")
    print("2.Current Account")
    account_type = input("Select account type (1 or 2): ")
    if account_type == "1":
        account_type = "SAVINGS"
    elif account_type == "2":
        account_type = "CURRENT"
    else:
        print("Invalid account type.")
        return
    pin = input("Set a 4-digit PIN for your account: ")
    confirm_pin = input("Confirm your PIN: ")
    if pin != confirm_pin:
        print("PINs do not match. Account creation failed.")
        return
    account = account_service.create_account(customer_id, account_type, pin)
    print("Account created successfully!")
    print(f"Account Number: {account.account_number}")
    
def main():
    connection = get_connection()
    create_tables(connection)

    customer_repository = CustomerRepository(connection)
    customer_service = CustomerService(customer_repository)
    account_repository = AccountRepository(connection)
    account_service = AccountService(account_repository)
    auth_service = AuthService(account_repository)
    transaction_repository = TransactionRepository(connection)
    transaction_service = TransactionService(transaction_repository, account_repository)
    
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_id = register(customer_service)
            if customer_id is not None:
                wants_account = input("Do you want to create an account? (y/n): ")
                if wants_account.lower() == "y":
                    create_account(customer_id, account_service)
        elif choice == "2":
            login(auth_service, transaction_service, account_service)
        elif choice == "3":
            print("Thank you for using the Banking Management System.")
            break
        else:
            print("Invalid choice.")

    connection.close()


if __name__ == "__main__":
    main()