import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API credentials from environment
api_token = os.getenv("WASSENGER_API_TOKEN")
device_id = os.getenv("WASSENGER_DEVICE_ID")

if not api_token or not device_id:
    raise RuntimeError(
        "WASSENGER_API_TOKEN or WASSENGER_DEVICE_ID is missing in the environment variables."
    )

# Contact creation URL and payload
url = f"https://api.wassenger.com/v1/chat/{device_id}/contacts"
headers = {"Content-Type": "application/json", "Token": api_token}

payload = [
    {
        "name": "Catherine",
        "surname": "Kimathi",
        "kind": "personal",
        "phone": "+254115470608",
        "country": "KE",
        "metadata": [{"key": "SOURCE", "value": "Otto.marketplace.lead"}],
    }
]

# Send request
response = requests.patch(url, json=payload, headers=headers)

# Output response
print("Contact:", response.status_code, response.json())
