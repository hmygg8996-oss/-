import tkinter as tk
from tkinter import messagebox
import requests
from shop.item_shop import buy_item
from database.db import get_inventory

# כתובת ה-Bot שלך (Flask או localhost)
BOT_URL = "http://127.0.0.1:5000/create_user"

class Launcher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SILVERIL Launcher")
        self.root.geometry("350x300")

        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login / Register", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Open Shop", command=self.open_shop).pack(pady=5)
        tk.Button(self.root, text="Open Inventory", command=self.open_inventory).pack(pady=5)

        self.user_id = None

        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # שולחים בקשה ל-Bot ליצור משתמש אם לא קיים
        try:
            response = requests.post(BOT_URL, json={"username": username, "password": password})
            if response.status_code == 200:
                self.user_id = self.get_user_id(username)
                messagebox.showinfo("Success", f"ברוך הבא {username}!")
            elif response.status_code == 400:
                # משתמש קיים, רק מאחזר את ה-user_id
                self.user_id = self.get_user_id(username)
                messagebox.showinfo("Login", f"ברוך הבא {username}!")
            else:
                messagebox.showerror("Error", "שגיאה ביצירת המשתמש.")
        except Exception as e:
            messagebox.showerror("Error", f"לא ניתן ליצור משתמש: {e}")

    def get_user_id(self, username):
        from database.db import get_user
        user = get_user(username)
        if user:
            return user[0]  # user_id
        return None

    def open_shop(self):
        if not self.user_id:
            messagebox.showerror("Error", "אנא התחבר קודם!")
            return

        shop_window = tk.Toplevel(self.root)
        shop_window.title("Shop")
        shop_window.geometry("300x300")

        items = ["Red Skin", "Blue Skin", "Sword"]
        for item in items:
            tk.Button(shop_window, text=item, command=lambda i=item: self.purchase(i)).pack(pady=5)

    def purchase(self, item_name):
        result = buy_item(self.user_id, item_name)
        messagebox.showinfo("Shop", result)

    def open_inventory(self):
        if not self.user_id:
            messagebox.showerror("Error", "אנא התחבר קודם!")
            return

        inventory_window = tk.Toplevel(self.root)
        inventory_window.title("Inventory")
        inventory_window.geometry("300x300")

        items = get_inventory(self.user_id)
        for item, qty in items.items():
            tk.Label(inventory_window, text=f"{item} x{qty}").pack()
