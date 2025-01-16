import requests

# টেলিগ্রাম বট টোকেন এবং চ্যানেল আইডি
TELEGRAM_TOKEN = "7589750623:AAHOOd3Wt39xH2vwnhYGh2Ujqz8-7uKG2d8"
CHAT_ID = "@trade_gtp"

# মেসেজ পাঠানোর ফাংশন
def send_message_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.text)

# উদাহরণ মেসেজ পাঠানো
send_message_to_telegram("Hello from GitHub Actions!")
