import requests

# টেলিগ্রাম বট টোকেন
TELEGRAM_TOKEN = "7589750623:AAHOOd3Wt39xH2vwnhYGh2Ujqz8-7uKG2d8"

# ব্যক্তিগত চ্যাট ID সংগ্রহ করার ফাংশন
def get_chat_id():
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    response = requests.get(url)
    if response.status_code == 200:
        updates = response.json()
        print("Updates:", updates)
        # এখানে JSON ডেটা থেকে chat_id সংগ্রহ করুন
    else:
        print("Failed to fetch updates:", response.text)

# মেসেজ পাঠানোর ফাংশন
def send_message_to_telegram(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.text)

# ব্যক্তিগত চ্যাট ID (getUpdates চালিয়ে ID পেতে হবে)
CHAT_ID = "YOUR_PERSONAL_CHAT_ID"  # এখানে আপনার chat_id বসান

# ব্যক্তিগত চ্যাট ID সংগ্রহ করার জন্য ফাংশন কল করুন (শুধু একবার চলবে)
# get_chat_id()

# মেসেজ পাঠানোর উদাহরণ
if CHAT_ID != "YOUR_PERSONAL_CHAT_ID":  # নিশ্চিত করুন যে আপনি chat_id আপডেট করেছেন
    send_message_to_telegram(CHAT_ID, "Hello! This is a direct message from your bot.")
else:
    print("Please update CHAT_ID with your personal chat ID!")
