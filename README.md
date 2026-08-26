# Banking Management System

A simple Banking Management System(CLI) built using Python, Object-Oriented Programming (OOP) concepts, and SQLite.

The application allows users to register customers, create bank accounts, perform banking transactions, manage account details, and store transaction history.

## Features

- Customer Registration
- Account Creation
- Savings Account
- Current Account
- Secure Login using PIN
- PIN Hashing using SHA-256
- View Profile
- Check Balance
- Deposit Money
- Withdraw Money
- Transfer Money Between Accounts
- Transaction History
- Change PIN
- Close Account
- Logout
- Input Validation and Error Handling

## Technologies Used

- Python
- SQLite
- Object-Oriented Programming (OOP)
- SHA-256 Hashing
- Git
- GitHub

## Project Structure

```text
banking-management-system/
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── schema.py
│
├── models/
│   ├── __init__.py
│   ├── account.py
│   ├── customer.py
│   └── transaction.py
│
├── repositories/
│   ├── __init__.py
│   ├── account_repository.py
│   ├── customer_repository.py
│   └── transaction_repository.py
│
├── services/
│   ├── __init__.py
│   ├── account_service.py
│   ├── auth_service.py
│   ├── customer_service.py
│   └── transaction_service.py
│
├── screenshots/
│   ├── main-menu.png
│   ├── account-menu.png
│   └── transaction-history.png
│
├── .gitignore
├── main.py
└── README.md
