import os
import sys
import requests

BASE_URL = "https://labs.hackthebox.com/api"

TOKEN = os.getenv("HTB_TOKEN")
if not TOKEN:
    print("[-] HTB_TOKEN not set in environment")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "htb-utils/1.0",
}

def get(endpoint, api_version="v4"):
    url = f"{BASE_URL}/{api_version}{endpoint}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()

def post(endpoint, json=None, api_version="v4"):
    url = f"{BASE_URL}/{api_version}{endpoint}"
    r = requests.post(url, headers=HEADERS, json=json, timeout=10)
    r.raise_for_status()
    return r.json()
