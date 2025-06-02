import requests
import csv
import os
from dotenv import load_dotenv
from itertools import islice
import logging

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Credentials
api_token = os.getenv("WASSENGER_API_TOKEN")
device_id = os.getenv("WASSENGER_DEVICE_ID")

# Validate
if not api_token or not device_id:
    logging.error("Missing API credentials in .env file.")
    exit(1)

# Constants
CSV_FILE = "create_dropped_leads.csv"
BASE_URL = f"https://api.wassenger.com/v1/chat/{device_id}/contacts"
HEADERS = {
    "Content-Type": "application/json",
    "Token": api_token
}

# Helper: Chunk list into batches of size n
def batch(iterable, n=10):
    iterable = iter(iterable)
    return iter(lambda: list(islice(iterable, n)), [])

# Build contact payloads from CSV
def load_contacts_from_csv(csv_file):
    contacts = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            contact_id = row["id"].strip()
            phone = row["phone"].strip()
            if contact_id and phone:
                contacts.append({
                    "name": contact_id,
                    "surname": "-",
                    "kind": "personal",
                    "phone": phone,
                    "country": "KE",
                    "metadata": [{"key": "SOURCE", "value": "Otto.lead"}]
                })
    return contacts

# Send contacts in batches
def send_contacts(contacts):
    for group in batch(contacts, 10):
        response = requests.patch(BASE_URL, json=group, headers=HEADERS)
        if response.status_code == 200:
            logging.info(f"=> Sent batch of {len(group)} contacts.")
        else:
            logging.error(f"=> Failed to send batch: {response.status_code}, {response.text}")

# Run it
contacts = load_contacts_from_csv(CSV_FILE)
send_contacts(contacts)
