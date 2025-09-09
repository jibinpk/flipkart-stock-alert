import requests
from bs4 import BeautifulSoup

# Flipkart product URL
URL = "https://www.flipkart.com/casio-ae-1200whd-1avdf-youth-digital-watch-men/p/itm170b0615f9472?pid=WATDJ5YXHRHZJFRY&lid=LSTWATDJ5YXHRHZJFRYVW2BZK&marketplace=FLIPKART&_refId=&_appId=CL"

# Telegram details
BOT_TOKEN = "Y7608314810:AAHfht53_lXPuyZoTFnO8MYP1gtHXI8zb6A"
CHAT_ID = "307434998"

def send_telegram(msg):
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                 params={"chat_id": CHAT_ID, "text": msg})

def check_stock():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    if "Add to cart" in r.text or "BUY NOW" in r.text.upper():
        send_telegram("✅ Casio AE-1200 is back in stock! 🔗 " + URL)
    else:
        print("Out of stock")

if __name__ == "__main__":
    check_stock()
