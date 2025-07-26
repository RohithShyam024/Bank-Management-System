import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="bank_db"
)
cursor = conn.cursor()

def create_account():
    name = input("Enter account holder name: ")
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name, 0.0))
    conn.commit()
    print("Account created successfully!")

def deposit():
    acc = int(input("Enter account number: "))
    amt = float(input("Enter deposit amount: "))
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_no = %s", (amt, acc))
    conn.commit()
    print("Deposit successful.")

def withdraw():
    acc = int(input("Enter account number: "))
    amt = float(input("Enter withdraw amount: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_no = %s", (acc,))
    data = cursor.fetchone()
    if data and data[0] >= amt:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_no = %s", (amt, acc))
        conn.commit()
        print("Withdrawal successful.")
    else:
        print("Insufficient balance or account not found.")

def view_account():
    acc = int(input("Enter account number: "))
    cursor.execute("SELECT * FROM accounts WHERE account_no = %s", (acc,))
    account = cursor.fetchone()
    if account:
        print(f"Account No: {account[0]}, Name: {account[1]}, Balance: ₹{account[2]}")
    else:
        print("Account not found.")

def delete_account():
    acc = int(input("Enter account number to delete: "))
    cursor.execute("DELETE FROM accounts WHERE account_no = %s", (acc,))
    conn.commit()
    print("Account deleted (if existed).")

def menu():
    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account\n2. Deposit\n3. Withdraw\n4. View Account\n5. Delete Account\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            view_account()
        elif choice == '5':
            delete_account()
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
    cursor.close()
    conn.close()
