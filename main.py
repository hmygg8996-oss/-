from auth.login import login_user
from lobby.ready import set_ready
from shop.item_shop import get_item_shop

def start_server():
    print("Fortnite Solo Backend Started")
    print(login_user("Player1"))
    print(get_item_shop())
    print(set_ready("Player1"))

if __name__ == "__main__":
    start_server()
