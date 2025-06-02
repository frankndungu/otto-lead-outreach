# Otto Lead Outreach Automation

This Python project helps Otto.rentals automate WhatsApp lead engagement using the [Wassenger API](https://wassenger.com/). It includes scripts for:

- Creating individual or bulk contacts
- Sending personalized WhatsApp messages
- Including booking links and KYC steps

## Features

- Add multiple or single contacts to your Wassenger device
- Send tailored messages including booking or KYC links
- Bulk outreach via CSV file
- Error handling with clear response logging
- All credentials managed securely using environment variables

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/frankndungu/otto-lead-outreach.git
cd otto-lead-outreach
```

### 2. Create a Virtual Environment 

```bash
python -m venv venv
venv/bin/activate   
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Environment Variables

Create a `.env` file in the root of the project with the following content:

```ini
WASSENGER_API_TOKEN=your_real_api_token
WASSENGER_DEVICE_ID=your_real_device_id
```

## Usage

### Sending a Single Message

Edit `send_message.py` and update the phone number/message, or run it as is for a quick test:

```bash
python send_message.py
```

### Sending Personalized Messages to a List

Update `named_leads.csv` with your contacts (columns: `name,phone`), then run:

```bash
python send_named_messages.py
```

### Sending Bulk Follow-up Messages

Add numbers to `followup.csv` (one phone number per line, or with a header), then run:

```bash
python send_follow_up_texts.py
```

### Creating Contacts 

Use a similar structure or add your own script for managing contacts as needed.

## Notes

- **All API keys and device IDs are managed via the `.env` file.**
- Logs and errors are printed to the terminal for easy debugging.
- See [Wassenger API Docs](https://wassenger.com/docs/) for more customization options.
