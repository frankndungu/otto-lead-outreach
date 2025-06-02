import requests
import csv
import os
from dotenv import load_dotenv
import logging

# Load .env variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Env variables
api_token = os.getenv("WASSENGER_API_TOKEN")
device_id = os.getenv("WASSENGER_DEVICE_ID")

# Validate
if not api_token or not device_id:
    logging.error("Missing API token or device ID.")
    exit(1)

# CSV file
CSV_FILE = "named_leads.csv"

# API setup
url = "https://api.wassenger.com/v1/messages"
headers = {
    "Content-Type": "application/json",
    "Authorization": api_token
}

def send_named_message(name, phone):
    message = (
        f"Hi {name}, this is Frank from Otto. I saw you were booking a car—"
        "just checking in to see if you still need help finishing up!"
    )
    payload = {
        "phone": phone,
        "message": message,
        "device": device_id
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        logging.info(f"=> Message sent to {name} ({phone})")
    except Exception as e:
        logging.error(f"=> Failed to send message to {name} ({phone}): {e}")

# Read CSV and send messages
with open(CSV_FILE, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"].strip()
        phone = row["phone"].strip()
        if name and phone:
            send_named_message(name, phone)
