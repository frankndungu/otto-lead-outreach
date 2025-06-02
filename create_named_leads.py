import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API credentials from environment variables
api_token = os.getenv("WASSENGER_API_TOKEN")
device_id = os.getenv("WASSENGER_DEVICE_ID")

if not api_token or not device_id:
    raise RuntimeError(
        "WASSENGER_API_TOKEN or WASSENGER_DEVICE_ID is missing in the environment variables."
    )

# Endpoint
url = f"https://api.wassenger.com/v1/chat/{device_id}/contacts"

# Headers
headers = {"Content-Type": "application/json", "Token": api_token}

# Payload with names
payload = [
    {
        "name": "Getachew",
        "surname": "Aberra",
        "kind": "personal",
        "phone": "+254740781551",
        "country": "KE",
        "metadata": [{"key": "SOURCE", "value": "Otto.lead"}],
    }
]

# Make request
response = requests.patch(url, json=payload, headers=headers)

print("Contact creation:", response.status_code)
print(response.json())
