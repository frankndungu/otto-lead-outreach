import requests
import csv
import os
import logging
from dotenv import load_dotenv
from time import sleep

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Get sensitive data from environment variables
api_token = os.getenv("WASSENGER_API_TOKEN")
device_id = os.getenv("WASSENGER_DEVICE_ID")

# Validate required environment variables
if not api_token or not device_id:
    logging.error("Missing API token or device ID in environment variables.")
    exit(1)

# Define constants
CSV_FILE = 'followup.csv'
WASSENGER_URL = 'https://api.wassenger.com/v1/messages'

# Prepare headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': api_token,
}

# Follow-up message to be sent
message_text = (
    "Hi again, just checking in — saw you tried to book a car on Otto but didn’t finish. "
    "Can I help you complete it today?"
)

def send_message(phone, retries=3):
    payload = {
        'phone': phone,
        'message': message_text,
        'device': device_id
    }
    for attempt in range(retries):
        try:
            response = requests.post(WASSENGER_URL, json=payload, headers=headers)
            response.raise_for_status()
            logging.info(f'Message sent to {phone}')
            return
        except Exception as e:
            logging.warning(f'Attempt {attempt + 1} failed for {phone}: {e}')
            sleep(2)
    logging.error(f'Failed to send message to {phone} after {retries} attempts.')

# Read numbers from CSV and send messages
with open(CSV_FILE, 'r') as file:
    reader = csv.reader(file)
    next(reader, None)  # Skip header row if present
    for row in reader:
        phone = row[0].strip()
        if phone:
            send_message(phone)
