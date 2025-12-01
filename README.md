Sure! Here is a clean, professional **README.md in English** for your project:

---

# Crypto Price Monitor (Async • SQLite • Logging)

This project is an asynchronous cryptocurrency price monitor built with **CoinGecko API**, **aiohttp**, **SQLite**, and **Python logging**.
It allows you to:

* fetch the current price of any cryptocurrency
* save price history in a local database
* view or delete saved history
* interact via a convenient CLI menu

---

## Features

### Real-time coin price fetching

The program fetches the USD price of any coin using the CoinGecko API.

### Automatic repeated requests

You can specify:

* how many times to fetch the price
* how many seconds to wait between each request

### SQLite database

All fetched prices are stored in:

```
storage/coins_price_history.db
```

You can:

* view the full history
* delete all entries

### Logging

All events are logged to:

```
crypto_parser/logs/app.log
```

---

# Project Structure

```
project/
│
├── crypto_parser/
│   ├── main.py                     # Main program logic
│   ├── config.py                   # API key and configuration
│   ├── logger_setup.py             # Logging setup
│   ├── storage.py                  # SQLite operations
│   ├── logs/
│   │   └── app.log                 # Log output
│   └── storage/
│       └── coins_price_history.db  # SQLite database
│
└── README.md
```

---

# Installation & Running

### 1. Install dependencies

```
pip install aiohttp
```

### 2. Add your CoinGecko API key

In `config.py`:

```python
API = "your_api_key_here"
```

A demo API key is supported, so no need to register.

### 3. Start the program

```
python main.py
```

---

# 🖥 Usage

After launching, the program shows a menu:

```
=== Coin price conclusion ===
1. Get the price of the coin
2. View price for previous uses
3. Delete all entries
4. Exit
```

## 1. Get coin price

You will be asked to enter:

* coin name (`bitcoin`, `ethereum`, `solana`...)
* number of times to fetch the price
* delay between calls

The program automatically logs the results and stores them in the database.

---

## 2. View price history

Displays all saved entries from the SQLite database.

---

## 3. Delete all entries

Completely clears the database.

---

## 4. Exit

Closes the program.

---

# Technologies Used

| Technology  | Purpose                          |
| ----------- | -------------------------------- |
| **asyncio** | asynchronous loops & delays      |
| **aiohttp** | HTTP requests to CoinGecko       |
| **SQLite**  | persistent price storage         |
| **logging** | writing logs to console and file |
| **Pathlib** | clean path/file handling         |

---

# Example Log Output

```
2025-05-19 14:22:11 - converter_logger - INFO - Coin: bitcoin | Price: 67321.52
2025-05-19 14:22:11 - converter_logger - ERROR - Enter the existing name of the coin!
```

---

# Possible Improvements

* reuse a single `aiohttp.ClientSession` across requests
* move menu UI into a separate module
* support tracking multiple coins simultaneously
* create a Telegram bot using **aiogram**
* add OOP architecture

---

If you want, I can:
✅ format this README beautifully with badges, colors, images
✅ generate a version for GitHub Pages
✅ add docstrings and inline documentation to your Python files
