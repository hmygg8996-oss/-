import sqlite3

# Paths to DB files
USERS_DB = "users.db"
INVENTORY_DB = "inventory.db"
STATS_DB = "stats.db"

# ----------------- USERS -----------------
def create_user(username, password):
    conn = sqlite3.connect(USERS_DB)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False  # שם משתמש קיים
    conn.close()
    return True

def get_user(username):
    conn = sqlite3.connect(USERS_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user


# ----------------- INVENTORY -----------------
def add_item(user_id, item_name, quantity=1):
    conn = sqlite3.connect(INVENTORY_DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT quantity FROM inventory WHERE user_id=? AND item_name=?", (user_id, item_name))
    result = cursor.fetchone()
    
    if result:
        new_quantity = result[0] + quantity
        cursor.execute("UPDATE inventory SET quantity=? WHERE user_id=? AND item_name=?", (new_quantity, user_id, item_name))
    else:
        cursor.execute("INSERT INTO inventory (user_id, item_name, quantity) VALUES (?, ?, ?)", (user_id, item_name, quantity))
    
    conn.commit()
    conn.close()

def remove_item(user_id, item_name, quantity=1):
    conn = sqlite3.connect(INVENTORY_DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT quantity FROM inventory WHERE user_id=? AND item_name=?", (user_id, item_name))
    result = cursor.fetchone()
    
    if result:
        new_quantity = result[0] - quantity
        if new_quantity <= 0:
            cursor.execute("DELETE FROM inventory WHERE user_id=? AND item_name=?", (user_id, item_name))
        else:
            cursor.execute("UPDATE inventory SET quantity=? WHERE user_id=? AND item_name=?", (new_quantity, user_id, item_name))
    
    conn.commit()
    conn.close()

def get_inventory(user_id):
    conn = sqlite3.connect(INVENTORY_DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT item_name, quantity FROM inventory WHERE user_id=?", (user_id,))
    items = cursor.fetchall()
    conn.close()
    
    return {item: qty for item, qty in items}


# ----------------- STATS -----------------
def add_kill(user_id, amount=1):
    conn = sqlite3.connect(STATS_DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT kills FROM stats WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    
    if result:
        new_kills = result[0] + amount
        cursor.execute("UPDATE stats SET kills=? WHERE user_id=?", (new_kills, user_id))
    else:
        cursor.execute("INSERT INTO stats (user_id, kills) VALUES (?, ?)", (user_id, amount))
    
    conn.commit()
    conn.close()

def add_win(user_id, amount=1):
    conn = sqlite3.connect(STATS_DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT wins FROM stats WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    
    if result:
        new_wins = result[0] + amount
        cursor.execute("UPDATE stats SET wins=? WHERE user_id=?", (new_wins, user_id))
    else:
        cursor.execute("INSERT INTO stats (user_id, wins) VALUES (?, ?)", (user_id, amount))
    
    conn.commit()
    conn.close()
