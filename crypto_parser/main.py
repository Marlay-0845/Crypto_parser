import asyncio
import aiohttp

from example_aiohttp.crypto_parser.config import *
from example_aiohttp.crypto_parser.logger_setup import setup_logger
import example_aiohttp.crypto_parser.storage as db


logger = setup_logger()


async def get_coin_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids={coin}&x_cg_demo_api_key={API}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            if response.status == 200:
                return await response.json()
            else:
                logger.error(f"Data not received! Status code: {response.status}")
            

async def main():
    while True:
        correct_coin = False 

        print("=== Coin price conclusion ===\n1. Get the price of the coin\n2. View price for previous uses\n3. Delete all entries\n4. Exit")
        try:
            user_choise = int(input("Enter your choice (1-4): "))
            if user_choise <= 0 or user_choise > 4:
                logger.error("Enter a number from 1 to 4!")
                continue
            
        except ValueError:
            pass
        
        try:
            if user_choise == 1:
                call_count = 0
                verification = False
                while True:
                    if verification:
                        break

                    try:
                        calls_count = int(input("How many calls do you want to receive: "))

                    except ValueError:
                        logger.error("Invalid input for amount. Please enter a numeric value.")
                        continue

                    try:
                        calls_pause = int(input("How many seconds is the pause between each call: "))    

                    except ValueError:
                        logger.error("Invalid input for amount. Please enter a numeric value.")
                        continue

                    verification = True

                while True:
                    if correct_coin is False:
                        coin = input("Enter a coin: ")
                        correct_coin = True
                    data = await get_coin_price(coin)
                    if not data or coin not in data:
                        correct_coin = False
                        logger.error("Enter the existing name of the coin!")
                        continue    
                    logger.info(f"Coin: {coin} | Price: {data[coin]['usd']}")
                    db.add_coin(coin, data[coin]['usd'])

                    call_count += 1
                    if call_count == calls_count:
                        await asyncio.sleep(5)
                        break

                    await asyncio.sleep(calls_pause)

            if user_choise == 2:
                notes = db.get_all_coins()

                for note in range(len(notes)):
                    print(notes[note])

                await asyncio.sleep(5)
            if user_choise == 3:
                db.delete_all_coins()
            
            if user_choise == 4:
                break
        except UnboundLocalError:
            logger.error("Invalid input for amount. Please enter a numeric value.")


asyncio.run(main())

