# Banking Management System

A simple Banking Management System(CLI) built using Python, Object-Oriented Programming (OOP) concepts, and SQLite.

The application allows users to register customers, create bank accounts, perform banking transactions, manage account details, and store transaction history.
<img width="596" height="211" alt="image" src="https://github.com/user-attachments/assets/6d9ba505-12de-4579-84b1-c241bd9af603" />
<img width="1607" height="857" alt="image" src="https://github.com/user-attachments/assets/26dbfaf3-3dc0-4734-8a22-82473f5f9a18" />
<img width="1607" height="516" alt="image" src="https://github.com/user-attachments/assets/318920aa-983f-41a0-a098-5ee70544ec90" />

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
