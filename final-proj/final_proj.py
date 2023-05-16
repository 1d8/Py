# Idea: Check a locally stored database for a password. If database doesn't exist, create it, then prompt for a password & add that password to database. If database does exist, get password & if it's correct, show a secret picture
# Todo:
# 1. Check if database table exists, if it doesn't create it (x)
# 2. Check if table contains any data, if it does prompt user for existing password & compare against that. Otherwise prompt password to be entered (x)


import sqlite3, os
import tkinter as tk
from tkinter import messagebox

def isTablePopulated(tableName):
    conn = sqlite3.connect("passwordDB")
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM {0}".format(tableName))
    result = cursor.fetchone()
    
    # close DB connection
    cursor.close()
    conn.close()

    # Check length of table data to ensure data is populated within table
    if result[0] > 0:
        return True
    else:
        return False

# Create table if it doesn't exist already
def checkIfTableExists():
    conn = sqlite3.connect("passwordDB")
    cursor = conn.cursor()
    # First check if database table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Passwords'")
    tResult = cursor.fetchone()
 

    if tResult is None:
        print("[+] Table doesn't exist! Creating it...")
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Passwords (password TEXT)
        ''')
    else:
        print("[+] Table exists. Continuing...")
    
    print("[+] Closing db connections...")
    cursor.close()
    conn.close()

def enterNewPassword():
    password = password_entry.get()
    conn = sqlite3.connect("passwordDB")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Passwords (password) VALUES (?)", (password,))
    conn.commit()

    cursor.close()
    conn.close()

    root.destroy()

def checkPassword(): # storedPassword is password grabbed from database
    # Get old password from db, compare them
    conn = sqlite3.connect("passwordDB")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Passwords")
     # row stores password from database
    row = cursor.fetchone()[0] #Only select the first element from the row, otherwise the formatting is weird. It'll be ('password',) otherwise
    cursor.close()
    conn.close()
    enteredPassword = password_entry.get()
    print("[+] Comparing {0}:{1}".format(row, enteredPassword))
    if row == enteredPassword:
        messagebox.showinfo("Success", "Password accepted!")
        root.destroy()
        secretWindow = tk.Tk()
        secretWindow.geometry("300x200")
        secretWindow.title("Secret window")
        text_label = tk.Label(secretWindow, text="Here are your secrets!\naGVsbG8gUHJvZmVzc29yIEJlY2VycmEhCg==")
        text_label.pack()
    else:
        messagebox.showerror("Error", "Incorrect password.")


checkIfTableExists()
print("[+] Checking if table is populated...")
if isTablePopulated("Passwords"):
    # If data exists in table, prompt user for existing password & compare it against password stored in db
    root = tk.Tk()
    root.geometry("300x100")
    root.title("Enter password")
    password_label = tk.Label(root, text="Enter password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    submit_button = tk.Button(root, text="Submit", command=checkPassword)
    submit_button.pack()
    root.mainloop()
else:
        # no data in table, prompt user for password, then populate that into table
    root = tk.Tk()
    root.geometry("300x100")
    root.title("New password")
    password_label = tk.Label(root, text="Enter new password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    submit_button = tk.Button(root, text="Submit", command=enterNewPassword)
    submit_button.pack()
    root.mainloop()