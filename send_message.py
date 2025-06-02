import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch API token from environment
api_token = os.getenv("WASSENGER_API_TOKEN")
if not api_token:
    raise RuntimeError("WASSENGER_API_TOKEN is not set in the environment")

# Message sending URL and headers
url = "https://api.wassenger.com/v1/messages"
headers = {"Content-Type": "application/json", "Token": api_token}

# Payload to send
message_payload = {
    "phone": "+254115470608",
    "message": (
        "Hello Catherine,\n\n"
        "Welcome to Otto! To move forward with your booking, we just need you to finish your profile "
        "with ID/license and your expected travel area. You can do that in the app easily by clicking "
        "the below link:\n\n"
        "https://app.otto.rentals/trip-details/3957f27c-06ad-483c-8b29-4efbc385a1a7?action=kyc-details\n\n"
        "Let me know if you have any troubles, 😊\n\n"
        "Frank - Otto"
    ),
}

# Send the request
response = requests.post(url, json=message_payload, headers=headers)

# Output
print("Message:", response.status_code, response.json())
