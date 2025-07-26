# 🏦 Bank Management System (MySQL Version)

A terminal-based banking system written in Python using MySQL.

## 🔧 Features
- Create Account
- Deposit/Withdraw
- View Account Details
- Delete Account

## 🛠 Tech Stack
- Python 3
- MySQL
- mysql-connector-python

## 🚀 How to Run

1. Set up your MySQL server and create the database:
```sql
CREATE DATABASE bank_db;
USE bank_db;
CREATE TABLE accounts (
    account_no INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    balance DOUBLE DEFAULT 0.0
);
```

2. Update the database credentials in `bank.py`:
```python
host="localhost",
user="your_username",
password="your_password",
database="bank_db"
```

3. Install connector if needed:
```bash
pip install mysql-connector-python
```

4. Run the script:
```bash
python bank.py
```
