import os
import requests
from bs4 import BeautifulSoup

URL = "https://www.flipkart.com/casio-ae-1200whd-1avdf-youth-digital-watch-men/p/itm170b0615f9472?pid=WATDJ5YXHRHZJFRY&lid=LSTWATDJ5YXHRHZJFRYVW2BZK&marketplace=FLIPKART&_refId=&_appId=CL"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.get(url, params={"chat_id": CHAT_ID, "text": msg})
    print("Telegram response:", r.text)  # debug

def check_stock():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    if "Add to cart" in r.text or "BUY NOW" in r.text.upper():
        send_telegram("✅ Casio AE-1200 is back in stock! 🔗 " + URL)
    else:
        print("Out of stock")

if __name__ == "__main__":
    # Test message
    send_telegram("🔔 Test: Flipkart Stock Alert Bot is working!")
    check_stock()
