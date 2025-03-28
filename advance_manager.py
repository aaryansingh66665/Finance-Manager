import os
import csv
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

FILE_NAME = 'transactions.csv'
USERS_FILE = 'users.csv'

def login_screen():
    """Displays the login screen."""
    window = tk.Tk()
    window.title("Finance Tracker")
    window.geometry("1024x800")  # Set the size of the window to 500x300 pixels
    window.configure(bg="#f0f0f0")  # Set the background color

    tk.Label(window, text="Finance Tracker", font=("Helvetica", 24), bg="#f0f0f0").place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    tk.Label(window, text="Username:", font=("Helvetica", 16), bg="#f0f0f0").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tk.Label(window, text="Password:", font=("Helvetica", 16), bg="#f0f0f0").place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    username_entry = tk.Entry(window, font=("Helvetica", 16))
    password_entry = tk.Entry(window, show="*", font=("Helvetica", 16))

    username_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    password_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    def login_user():
        """Logs in the user."""
        username = username_entry.get()
        password = password_entry.get()
        if check_credentials(username, password):
            main_screen(username)
        else:
            messagebox.showerror("Invalid Credentials", "Invalid username or password.")

    tk.Button(window, text="Login", command=login_user, font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", padx=10, pady=5).place(relx=0.4, rely=0.5, anchor=tk.CENTER)
    tk.Button(window, text="Register", command=register_user_screen, font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", padx=10, pady=5).place(relx=0.6, rely=0.5, anchor=tk.CENTER)

    window.mainloop()

def register_user_screen():
    """Displays the register user screen."""
    window = tk.Tk()
    window.title("Finance Tracker")
    window.geometry("600x400")  # Set the size of the window to 500x350 pixels
    window.configure(bg="#f0f0f0")  # Set the background color

    tk.Label(window, text="Finance Tracker", font=("Helvetica", 24), bg="#f0f0f0").place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    tk.Label(window, text="Username:", font=("Helvetica", 16), bg="#f0f0f0").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tk.Label(window, text="Password:", font=("Helvetica", 16), bg="#f0f0f0").place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    tk.Label(window, text="Confirm Password:", font=("Helvetica", 16), bg="#f0f0f0").place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    username_entry = tk.Entry(window, font=("Helvetica", 16))
    password_entry = tk.Entry(window, show="*", font=("Helvetica", 16))
    confirm_password_entry = tk.Entry(window, show="*", font=("Helvetica", 16))

    username_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    password_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    confirm_password_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    def register_user():
        """Registers a new user."""
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        if password == confirm_password:
            if not check_username_exists(username):
                with open(USERS_FILE, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([username, password])
                messagebox.showinfo("User  Registered", "User  registered successfully!")
                login_screen()
            else:
                messagebox.showerror("Username Exists", "Username already exists.")
        else:
            messagebox.showerror("Password Mismatch", "Passwords do not match.")

    tk.Button(window, text="Register", command=register_user, font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", padx=10, pady=5).place(relx=0.4, rely=0.6, anchor=tk.CENTER)
    tk.Button(window, text="Back", command=login_screen, font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", padx=10, pady=5).place(relx=0.6, rely=0.6, anchor=tk.CENTER)

    window.mainloop()

def main_screen(username):
    """Displays the main screen."""
    window = tk.Tk()
    window.title("Finance Tracker")
    window.geometry("500x300")  # Set the size of the window to 500x300 pixels
    window.configure(bg="#f0f0f0")  # Set the background color

    def add_transaction_screen():
        """Displays the add transaction screen."""
        window.destroy()
        add_transaction_window = tk.Tk()
        add_transaction_window.title("Finance Tracker")
        add_transaction_window.geometry("500x250")  # Set the size of the window to 500x250 pixels
        add_transaction_window.configure(bg="#f0f0f0")  # Set the background color

        tk.Label(add_transaction_window, text="Date (YYYY-MM-DD):", font=("Helvetica", 16), bg="#f0f0f0").place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        tk.Label(add_transaction_window, text="Description:", font=("Helvetica", 16), bg="#f0f0f0").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        tk.Label(add_transaction_window, text="Amount:", font=("Helvetica", 16), bg="#f0f0f0").place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        date_entry = tk.Entry(add_transaction_window, font=("Helvetica", 16))
        description_entry = tk.Entry(add_transaction_window, font=("Helvetica", 16))
        amount_entry = tk.Entry(add_transaction_window, font=("Helvetica", 16))

        date_entry.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        description_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        amount_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        def add_transaction():
            """Adds a new transaction."""
            date = date_entry.get()
            description = description_entry.get()
            amount = amount_entry.get()
            try:
                datetime.strptime(date, "%Y-%m-%d")
                float(amount)
                with open(FILE_NAME, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([username, date, description, amount])
                messagebox.showinfo("Transaction Added", "Transaction added successfully!")
                main_screen(username)
            except ValueError:
                messagebox.showerror("Invalid Date or Amount", "Please enter a valid date (YYYY-MM-DD) and amount.")

        tk.Button(add_transaction_window, text="Add Transaction", command=add_transaction, font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", padx=10, pady=5).place(relx=0.4, rely=0.5, anchor=tk.CENTER)
        tk.Button(add_transaction_window, text="Back", command=lambda: main_screen(username), font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", padx=10, pady=5).place(relx=0.6, rely=0.5, anchor=tk.CENTER)

        add_transaction_window.mainloop()

    def view_transactions():
        """Displays the view transactions screen."""
        window.destroy()
        view_transactions_window = tk.Tk()
        view_transactions_window.title("Finance Tracker")
        view_transactions_window.geometry("500x400")  # Set the size of the window to 500x400 pixels
        view_transactions_window.configure(bg="#f0f0f0")  # Set the background color

        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            row_num = 0
            for row in reader:
                if row[0] == username:
                    tk.Label(view_transactions_window, text=f"{row[1]} {row[2]} {row[3]}", font=("Helvetica", 16), bg="#f0f0f0").place(relx=0.5, rely=0.1 + row_num * 0.05, anchor=tk.CENTER)
                    row_num += 1
            if row_num == 0:
                tk.Label(view_transactions_window, text="No transactions found.", font=("Helvetica", 16), bg="#f0f0f0").place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Button(view_transactions_window, text="Back", command=lambda: main_screen(username), font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", padx=10, pady=5).place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        view_transactions_window.mainloop()

    tk.Button(window, text="Add Transaction", command=add_transaction_screen, font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", padx=10, pady=5).place(relx=0.4, rely=0.4, anchor=tk.CENTER)
    tk.Button(window, text="View Transactions", command=view_transactions, font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", padx=10, pady=5).place(relx=0.6, rely=0.4, anchor=tk.CENTER)
    tk.Button(window, text="Logout", command=login_screen, font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", padx=10, pady=5).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    window.mainloop()

def check_credentials(username, password):
    """Checks the user's credentials."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
    return False

def check_username_exists(username):
    """Checks if the username exists."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    return True
    return False

if __name__ == "__main__":
    login_screen()