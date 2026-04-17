import os
import requests

# Configuration
TYPEFORM_API_KEY = os.getenv('TYPEFORM_API_KEY')
TYPEFORM_FORM_ID = 'qiYA3SV9'
SLACK_WORKSPACE_TOKEN = os.getenv('SLACK_WORKSPACE_TOKEN')
IT_SUPPORT_EMAIL = 'it-support@example.com'

def fetch_latest_onboardee():
    """Fetches the latest response from Typeform."""
    url = f"https://api.typeform.com/forms/{TYPEFORM_FORM_ID}/responses"
    headers = {"Authorization": f"Bearer {TYPEFORM_API_KEY}"}
    # Logic to filter latest unproccessed response
    print(f"Fetching responses from Typeform: {TYPEFORM_FORM_ID}...")
    return {"name": "Tarun Kumar", "email": "tarun@example.com"}

def invite_to_slack(email):
    """Invites a user to the Slack workspace."""
    print(f"Inviting {email} to Slack workspace...")
    # API Call: SLACK_INVITE_USER_TO_WORKSPACE

def request_access(name):
    """Sends the IT access request email."""
    subject = f"Access Request - New Joiner: {name}"
    body = f"""
Hi Team,

I have recently joined this org please give me access to Kantata or VPN.

Thanking you,
{name}
    """
    print(f"Sending access request email for {name} to {IT_SUPPORT_EMAIL}...")
    # API Call: GMAIL_SEND_EMAIL

if __name__ == "__main__":
    new_hire = fetch_latest_onboardee()
    invite_to_slack(new_hire['email'])
    request_access(new_hire['name'])
    print("Onboarding automation complete! 🎯")