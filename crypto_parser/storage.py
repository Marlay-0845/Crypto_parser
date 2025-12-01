import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


data_dir = BASE_DIR / "storage"
data_dir.mkdir(exist_ok=True)

file_path = data_dir / "coins_price_history.db"


with sqlite3.connect(file_path) as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS coins_list(
        coin_name TEXT,
        coin_price REAL,
        create_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")


def add_coin(coin_name, coin_price):
    with sqlite3.connect(file_path) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO coins_list (coin_name, coin_price) VALUES (?, ?);", (coin_name, coin_price))
        db.commit()


def get_all_coins():
    with sqlite3.connect(file_path) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM coins_list")
        return cursor.fetchall()


def delete_all_coins():
    with sqlite3.connect(file_path) as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM coins_list")
        db.commit()
