import os
import time
import sys

# --- CONFIGURATION ---
DEMO_MODE = True
TYPEFORM_API_KEY = os.getenv('TYPEFORM_API_KEY', 'demo_key')
TYPEFORM_FORM_ID = 'qiYA3SV9'
IT_SUPPORT_EMAIL = 'it-support@example.com'

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def log(tag, message, color=Colors.OKBLUE):
    # Using .encode().decode() to handle terminal encoding issues safely
    safe_message = message.encode('utf-8', 'replace').decode('utf-8')
    print(f"{color}[{tag}]{Colors.ENDC} {safe_message}")

def fetch_latest_onboardee():
    log("SYNC", f"Checking Typeform {TYPEFORM_FORM_ID} for new responses...")
    time.sleep(1.5)
    log("DATA", "New response detected: Tarun Kumar (tarun@example.com)", Colors.OKGREEN)
    return {"name": "Tarun Kumar", "email": "tarun@example.com"}

def invite_to_slack(email):
    log("SLACK", f"Initiating workspace invite for {email}...")
    time.sleep(1)
    log("SUCCESS", f"Invite sent to {email}! [Invite Sent]", Colors.OKGREEN)

def request_access(name):
    log("GMAIL", f"Drafting IT access request for {name}...")
    time.sleep(1)
    log("MAIL", f"To: {IT_SUPPORT_EMAIL}")
    log("SUCCESS", f"Email sent via Jujubee (Wingman)! [Rocket]", Colors.OKGREEN)

if __name__ == '__main__':
    # Ensure output is UTF-8 if supported
    if sys.stdout.encoding != 'utf-8':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'replace')

    print(f'\n{Colors.BOLD}{Colors.HEADER}=== wingHR: Onboarding Wingman Demo ==={Colors.ENDC}\n')
    new_hire = fetch_latest_onboardee()
    print('-' * 40)
    invite_to_slack(new_hire['email'])
    print('-' * 40)
    request_access(new_hire['name'])
    print('-' * 40)
    print(f'\n{Colors.BOLD}{Colors.OKGREEN}Onboarding automation complete! [Done]{Colors.ENDC}\n')