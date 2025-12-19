import tkinter as tk
from tkinter import messagebox
from database.db import get_inventory
from shop.item_shop import buy_item

def open_shop(user_id):
    shop_window = tk.Tk()
    shop_window.title("Shop")
    shop_window.geometry("300x300")

    def purchase(item_name):
        result = buy_item(user_id, item_name)
        messagebox.showinfo("Shop", result)

    for item in ["Red Skin", "Blue Skin", "Sword"]:
        tk.Button(shop_window, text=item, command=lambda i=item: purchase(i)).pack(pady=5)

    shop_window.mainloop()
