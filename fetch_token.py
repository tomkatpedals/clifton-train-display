import requests
import json
import os

username = os.getenv("NJTRANSIT_USERNAME")
password = os.getenv("NJTRANSIT_PASSWORD")

url = "https://api.njtransit.com/oauth2/token"


headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "grant_type": "client_credentials"
}

print("Requesting token...")

response = requests.post(auth_url, data=payload, auth=(username, password), headers=headers)

if response.status_code == 200:
    token_data = response.json()
    with open("token.json", "w") as f:
        json.dump(token_data, f, indent=2)
    print("Token saved to token.json")
else:
    print("Failed to get token:", response.status_code, response.text)
    raise SystemExit(1)
