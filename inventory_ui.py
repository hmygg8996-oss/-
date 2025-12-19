import tkinter as tk
from tkinter import messagebox
import requests  # נשתמש לשליחת בקשה ל-Discord Bot
from database.db import get_user

BOT_URL = "http://127.0.0.1:5000/create_user"  # כאן כתובת ה-Bot שלך או Flask API

def login(username, password):
    user = get_user(username)
    if user:
        if user[2] == password:
            messagebox.showinfo("Login", f"ברוך הבא {username}!")
            return True
        else:
            messagebox.showerror("Login", "סיסמה שגויה.")
            return False
    else:
        # המשתמש לא קיים → שולחים בקשה ל-Bot ליצור אותו
        try:
            response = requests.post(BOT_URL, json={"username": username, "password": password})
            if response.status_code == 200:
                messagebox.showinfo("Register", f"המשתמש {username} נוצר בהצלחה!")
                return True
            else:
                messagebox.showerror("Register", "שגיאה ביצירת המשתמש.")
                return False
        except Exception as e:
            messagebox.showerror("Error", f"לא ניתן ליצור משתמש: {e}")
            return False

# --- GUI ---
root = tk.Tk()
root.title("Launcher")
root.geometry("300x200")

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

def on_login():
    username = username_entry.get()
    password = password_entry.get()
    if login(username, password):
        root.destroy()
        # כאן תוכל לפתוח Shop או Inventory

tk.Button(root, text="Login / Register", command=on_login).pack(pady=10)

root.mainloop()
