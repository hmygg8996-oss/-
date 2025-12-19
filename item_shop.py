from database.db import add_item, get_inventory


SHOP_ITEMS = {
    "Red Skin": 100,
    "Blue Skin": 150,
    "Sword": 200
}

def buy_item(user_id, item_name):

    if item_name not in SHOP_ITEMS:
        return f"❌ הפריט '{item_name}' לא קיים בחנות."

    inventory = get_inventory(user_id)
    if item_name in inventory:
        return f"⚠️ כבר יש לך את הפריט '{item_name}'."
    
    add_item(user_id, item_name)
    return f"✅ רכשת את '{item_name}' בהצלחה!"
