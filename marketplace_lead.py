import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch API token and device ID from environment
api_token = os.getenv("WASSENGER_API_TOKEN")
device_id = os.getenv("WASSENGER_DEVICE_ID")

if not api_token:
    raise RuntimeError("WASSENGER_API_TOKEN is not set in the environment")
if not device_id:
    raise RuntimeError("WASSENGER_DEVICE_ID is not set in the environment")

# Step 1: Create the contact
contact_url = f"https://api.wassenger.com/v1/chat/{device_id}/contacts"
contact_payload = {
    "name": "Willis",
    "surname": "Gitau",
    "kind": "personal",
    "phone": "+254111456992",
    "country": "KE",
    "metadata": [{"key": "SOURCE", "value": "Otto.marketplace.lead"}],
}
headers = {"Content-Type": "application/json", "Token": api_token}

create_response = requests.patch(contact_url, json=[contact_payload], headers=headers)
print("Contact:", create_response.status_code, create_response.json())

# Step 2: Send message
message_text = (
    "Hello Willis,\n\n"
    "Welcome to Otto! To move forward with your booking, we just need you to finish your profile with ID/license and your expected travel area. "
    "You can do that in the app easily by clicking the below link:\n\n"
    "https://app.otto.rentals/trip-details/197aaac9-1c62-478e-8d8b-b586eaaeb64a?action=kyc-details\n\n"
    "Let me know if you have any troubles, 😊\n\n"
    "Frank - Otto"
)

message_url = "https://api.wassenger.com/v1/messages"
message_payload = {"phone": "+254111456992", "message": message_text}

message_response = requests.post(message_url, json=message_payload, headers=headers)
print("Message:", message_response.status_code, message_response.json())
