import csv
import os
import getpass
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

FILE_NAME = 'transactions.csv'
USERS_FILE = 'users.csv'

class FinanceTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Finance Tracker")
        self.window.geometry("1080x720")  # Set the window size to 1080x720
        self.username = None

        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.window, text="Finance Tracker", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        tk.Label(self.window, text="Username:", font=("Arial", 18)).grid(row=1, column=0, padx=20, pady=10)
        tk.Label(self.window, text="Password:", font=("Arial", 18)).grid(row=2, column=0, padx=20, pady=10)

        self.username_entry = tk.Entry(self.window, font=("Arial", 18), width=30)
        self.password_entry = tk.Entry(self.window, font=("Arial", 18), show="*", width=30)

        self.username_entry.grid(row=1, column=1, padx=20, pady=10)
        self.password_entry.grid(row=2, column=1, padx=20, pady=10)

        tk.Button(self.window, text="Login", font=("Arial", 18), command=self.login_user).grid(row=3, column=0, padx=20, pady=10)
        tk.Button(self.window, text="Register", font=("Arial", 18), command=self.register_user_screen).grid(row=3, column=1, padx=20, pady=10)

    def register_user_screen(self):
        self.clear_screen()
        tk.Label(self.window, text="Finance Tracker", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        tk.Label(self.window, text="Username:", font=("Arial", 18)).grid(row=1, column=0, padx=20, pady=10)
        tk.Label(self.window, text="Password:", font=("Arial", 18)).grid(row=2, column=0, padx=20, pady=10)
        tk.Label(self.window, text="Confirm Password:", font=("Arial", 18)).grid(row=3, column=0, padx=20, pady=10)

        self.username_entry = tk.Entry(self.window, font=("Arial", 18), width=30)
        self.password_entry = tk.Entry(self.window, font=("Arial", 18), show="*", width=30)
        self.confirm_password_entry = tk.Entry(self.window, font=("Arial", 18), show="*", width=30)

        self.username_entry.grid(row=1, column=1, padx=20, pady=10)
        self.password_entry.grid(row=2, column=1, padx=20, pady=10)
        self.confirm_password_entry.grid(row=3, column=1, padx=20, pady=10)

        tk.Button(self.window, text="Register", font=("Arial", 18), command=self.register_user).grid(row=4, column=0, padx=20, pady=10)
        tk.Button(self.window, text="Back", font=("Arial", 18), command=self.login_screen).grid(row=4, column=1, padx=20, pady=10)

    def main_screen(self):
        self.clear_screen()
        tk.Label(self.window, text="Finance Tracker", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        tk.Button(self.window, text="Add Transaction", font=("Arial", 18), command=self.add_transaction_screen).grid(row=1, column=0, padx=20, pady=10)
        tk.Button(self.window, text="View Transactions", font=("Arial", 18), command=self.view_transactions).grid(row=1, column=1, padx=20, pady=10)
        tk.Button(self.window, text="Delete All Transactions", font=("Arial", 18), command=self.delete_transactions).grid(row=2, column=0, padx=20, pady=10)
        tk.Button(self.window, text="Logout", font=("Arial", 18), command=self.login_screen).grid(row=2, column=1, padx=20, pady=10)

    def add_transaction_screen(self):
        self.clear_screen()
        tk.Label(self.window, text="Finance Tracker", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        tk.Label(self.window, text="Date (YYYY-MM-DD):", font=("Arial", 18)).grid(row=1, column=0, padx=20, pady=10)
        tk.Label(self.window, text="Description:", font=("Arial", 18)).grid(row=2, column=0, padx=20, pady=10)
        tk.Label(self.window, text="Amount (negative for debit, positive for credit):", font=("Arial", 18)).grid(row=3, column=0, padx=20, pady=10)

        self.date_entry = tk.Entry(self.window, font=("Arial", 18), width=30)
        self.description_entry = tk.Entry(self.window, font=("Arial", 18), width=30)
        self.amount_entry = tk.Entry(self.window, font=("Arial", 18), width=30)

        self.date_entry.grid(row=1, column=1, padx=20, pady=10)
        self.description_entry.grid(row=2, column=1, padx=20, pady=10)
        self.amount_entry.grid(row=3, column=1, padx=20, pady=10)

        tk.Button(self.window, text="Add Transaction", font=("Arial", 18), command=self.add_transaction).grid(row=4, column=0, padx=20, pady=10)
        tk.Button(self.window, text="Back", font=("Arial", 18), command=self.main_screen).grid(row=4, column=1, padx=20, pady=10)

    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def add_transaction(self):
        date = self.date_entry.get()
        description = self.description_entry.get()
        amount = float(self.amount_entry.get())
        self.add_transaction_to_file(date, description, amount, self.username)
        messagebox.showinfo("Transaction Added", "Transaction added successfully!")
        self.main_screen()

    def add_transaction_to_file(self, date, description, amount, username):
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, date, description, amount])

    def view_transactions(self):
        self.clear_screen()
        tk.Label(self.window, text="Finance Tracker", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        tk.Label(self.window, text="Date\t\tDescription\t\tAmount", font=("Arial", 18)).grid(row=1, column=0, columnspan=2, padx=20, pady=10)
        tk.Label(self.window, text="-" * 40, font=("Arial", 18)).grid(row=2, column=0, columnspan=2, padx=20, pady=10)

        dates = []
        amounts = []
        total_debit = 0
        total_credit = 0
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            row_num = 3
            for row in reader:
                if row[0] == self.username:
                    tk.Label(self.window, text=f"{row[1]}\t{row[2]}\t\t{row[3]}", font=("Arial", 18)).grid(row=row_num, column=0, columnspan=2, padx=20, pady=10)
                    row_num += 1
                    amount = float(row[3])
                    dates.append(row[1])
                    amounts.append(amount)
                    if amount < 0:
                        total_debit += abs(amount)
                    else:
                        total_credit += amount

        tk.Label(self.window, text="-" * 40, font=("Arial", 18)).grid(row=row_num, column=0, columnspan=2, padx=20, pady=10)
        tk.Label(self.window, text=f"Total Debit: {total_debit:.2f}", font=("Arial", 18)).grid(row=row_num + 1, column=0, columnspan=2, padx=20, pady=10)
        tk.Label(self.window, text=f"Total Credit: {total_credit:.2f}", font=("Arial", 18)).grid(row=row_num + 2, column=0, columnspan=2, padx=20, pady=10)
        tk.Label(self.window, text=f"Net Balance: {total_credit - total_debit:.2f}", font=("Arial", 18)).grid(row=row_num + 3, column=0, columnspan=2, padx=20, pady=10)

        tk.Button(self.window, text="View Graph", font=("Arial", 18), command=lambda: self.view_graph(dates, amounts)).grid(row=row_num + 4, column=0, columnspan=2, padx=20, pady=10)
        tk.Button(self.window, text="Back", font=("Arial", 18), command=self.main_screen).grid(row=row_num + 5, column=0, columnspan=2, padx=20, pady=10)

    def view_graph(self, dates, amounts):
        plt.figure(figsize=(10, 5))
        plt.plot(dates, amounts, marker='o')
        plt.title("Expense Graph")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.grid(True)
        plt.show()

    def delete_transactions(self):
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)
            messagebox.showinfo("Transactions Deleted", "All transactions deleted successfully!")
        else:
            messagebox.showinfo("No Transactions", "No transactions to delete.")

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.check_credentials(username, password):
            self.username = username
            self.main_screen()
        else:
            messagebox.showerror("Invalid Credentials", "Invalid username or password.")

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if password == confirm_password:
            self.add_user_to_file(username, password)
            messagebox.showinfo("User  Registered", "User  registered successfully!")
            self.login_screen()
        else:
            messagebox.showerror("Password Mismatch", "Passwords do not match.")

    def check_credentials(self, username, password):
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == username and row[1] == password:
                        return True
        return False

    def add_user_to_file(self, username, password):
        with open(USERS_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

if __name__ == "__main__":
    app = FinanceTracker()
    app.window.mainloop()
