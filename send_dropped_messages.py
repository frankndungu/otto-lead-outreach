import requests
import csv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get sensitive data from environment variables
api_token = os.getenv("WASSENGER_API_TOKEN")
device_id = os.getenv("WASSENGER_DEVICE_ID")

# Define constants
CSV_FILE = 'dropped_leads.csv'
WASSENGER_URL = 'https://api.wassenger.com/v1/messages'

# Prepare headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': api_token,
}

# Final message to be sent
message_text = (
    "Hi there,\n\n"
    "This is Frank from Otto. I saw you tried to book a car but didn’t finish—"
    "Otto makes it easy to hire vehicles from trusted partners with clear pricing and no surprises. "
    "Do you need help completing your booking?"
)

def send_message(phone):
    payload = {
        'phone': phone,
        'message': message_text,
        'device': device_id
    }
    try:
        response = requests.post(WASSENGER_URL, json=payload, headers=headers)
        response.raise_for_status()
        print(f'=> Message sent to {phone}')
    except Exception as e:
        print(f'Failed to send message to {phone}: {e}')

# Read numbers from CSV and send messages
with open(CSV_FILE, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        phone = row[0].strip()
        send_message(phone)
