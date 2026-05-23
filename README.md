 PyBank ATM System

A beginner-friendly ATM Banking System built with Python that simulates real-world banking operations such as account registration, secure login, deposits, withdrawals, and money transfers.

This project demonstrates the use of Python programming, file handling, hashing for security, object-oriented programming (OOP), and transaction management.

---

 Features

✅ User Registration  
✅ Secure Login System  
✅ PIN Encryption using SHA-256 Hashing  
✅ Automatic Account Number Generation  
✅ Deposit Money  
✅ Withdraw Money  
✅ Transfer Money Between Accounts  
✅ File-Based Account Storage  
✅ Transaction Recording

---

 Technologies Used

- **Python**
- **CSV File Handling**
- **Object-Oriented Programming (OOP)**
- **SHA-256 Hashing**
- **Random Account Number Generation**
- **Datetime Module**

---

 Project Structure

```bash
PyBank ATM/
│── main.py                  # Main program and menu system
│── account.py               # Registration and login logic
│── transaction.py           # Banking transactions
│── account_balances.txt     # Stores account information
│── transactions.txt         # Stores transaction history
```

---

 How It Works

1️⃣ Registration
Users create an account by entering:

- Phone Number
- PIN

The system then:

- Encrypts the PIN using **SHA-256**
- Generates a random account number
- Saves account details securely

2️⃣ Login
Users log in using:

- Phone Number
- PIN

The system verifies credentials by comparing the encrypted PIN.

 3️⃣ Banking Transactions
After logging in, users can:

💰 Deposit money  
🏧 Withdraw money  
🔁 Transfer money to another account

Balances are updated automatically and stored in files.

---

## 🔐 Security Features

This project uses **SHA-256 hashing** to encrypt user PINs instead of storing them in plain text.

Example:

```python
hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
```

This improves security and simulates how real banking systems protect sensitive information.

---

 How To Run The Project

1. Clone this repository

```bash
git clone YOUR_GITHUB_LINK
```

2. Open the project folder

```bash
cd pybank-atm-system
```

3. Run the program

```bash
python main.py
```

---

Sample Menu

```text
===== PyBank ATM =====
1. Register
2. Login
3. Exit
```

After Login:

```text
--- Menu ---
1. Deposit
2. Withdraw
3. Transfer
4. Logout
```

---

What I Learned

Through this project, I improved my understanding of:

- Python functions
- File handling
- Object-Oriented Programming
- Authentication systems
- Hashing and security concepts
- Transaction logic

---

 Future Improvements

- GUI version using Tkinter
- Database integration (SQLite/MySQL)
- Email/SMS notifications
- Balance checking feature
- Admin dashboard

---

 Author

Aphelele Somani






