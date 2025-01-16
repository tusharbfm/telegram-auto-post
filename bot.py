import requests

# টেলিগ্রাম বট টোকেন এবং চ্যানেল আইডি
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHANNEL_ID"

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
