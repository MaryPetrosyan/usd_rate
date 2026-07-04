# 💱 Rate.am Currency Parser Telegram Bot

A Telegram bot that parses exchange rates from Rate.am using Selenium and returns the best available exchange rate for selected currencies.

## Features

* Parses exchange rates directly from Rate.am
* Supports:

  * USD
  * EUR
  * RUR
* Telegram bot interface with inline keyboard buttons
* Automatically finds and returns the lowest exchange rate for the selected currency
* Environment variable support using `.env`

---

## Technologies Used

* Python
* Selenium
* PyTelegramBotAPI (telebot)
* python-dotenv
* Google Chrome
* ChromeDriver

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rate-am-parser-bot.git
cd rate-am-parser-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install selenium pytelegrambotapi python-dotenv
```

---

## Create a Telegram Bot

1. Open Telegram.
2. Search for **@BotFather**.
3. Run:

```text
/start
```

4. Create a new bot:

```text
/ newbot
```

5. Follow the instructions.
6. Copy the generated bot token.

---

## Configure Environment Variables

Create a `.env` file in the project root:

```env
TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

Example:

```env
TOKEN=123456789:AAExampleToken
```

---

## How It Works

### Step 1

The script opens the Rate.am exchange rates page using Selenium.

```python
driver.get(
    "https://www.rate.am/hy/armenian-dram-exchange-rates/banks"
)
```

### Step 2

The user starts the bot with:

```text
/start
```

### Step 3

The bot displays three currency options:

* USD
* EUR
* RUR

### Step 4

After selecting a currency, Selenium parses the corresponding column from the Rate.am table.

### Step 5

All available rates are collected into a list.

```python
arr.append(float(element.text))
```

### Step 6

The rates are sorted and the lowest value is returned.

```python
arr.sort()
return arr[0]
```

### Step 7

The bot sends the result back to the user.

Example:

```text
USD: 384.5
```

---

## Project Structure

```text
project/
│
├── main.py
├── .env
├── README.md
└── requirements.txt
```

---

## Running the Bot

```bash
python main.py
```

The bot will start polling Telegram updates and wait for user requests.

---

## Example Usage

```text
User: /start

Bot:
Choose a currency 👇

[USD] [EUR] [RUR]

User clicks USD

Bot:
USD: 384.5
```

---

## Notes

* Chrome browser must be installed.
* ChromeDriver version should match your Chrome version.
* Website structure changes on Rate.am may require updating the CSS selectors.
* Internet connection is required for scraping and Telegram communication.


National Polytechnic University of Armenia
