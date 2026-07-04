from telebot import TeleBot , types
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from dotenv import load_dotenv
import os
load_dotenv()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.rate.am/hy/armenian-dram-exchange-rates/banks')
time.sleep(3)


def func(driver, currency):
    arr = []
    if currency.upper() == 'USD':
        col = 1
    elif currency.upper() == 'EUR':
        col = 2
    elif currency.upper() == 'RUR':
        col = 3
    else:
        print('NOT FOUND')
        return None
    for i in range(1, 18):
        try:
            selector = f"div:nth-child({i}) > div:nth-child({col}) > div:nth-child(2) > div > div"
            element = driver.find_element(By.CSS_SELECTOR,selector)
            arr.append(float(element.text))
        except Exception as ex:
            print(ex.__class__.__name__)
    arr.sort()
    return arr[0] if arr else None


TOKEN = os.getenv("TOKEN")
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def run_bot(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton("USD", callback_data="USD")
    btn2 = types.InlineKeyboardButton("EUR", callback_data="EUR")
    btn3 = types.InlineKeyboardButton("RUR", callback_data="RUR")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Ընտրի արժույթը 👇", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    currency = call.data
    res = func(driver, currency)
    if res:
        bot.send_message(call.message.chat.id, f"{currency}: {res}")
    else:
        bot.send_message(call.message.chat.id, "Տվյալները չգտնվեցին")


try:
    bot.polling()
except KeyboardInterrupt:
    print("Bot stopped by user.")
finally:
    driver.quit()
 