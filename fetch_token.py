import os
import requests

username = os.getenv("NJTRANSIT_USERNAME")
password = os.getenv("NJTRANSIT_PASSWORD")

print("Requesting token...")

response = requests.post(
    "https://raildata.njtransit.com/api/GTFSRT/getToken",
    headers={"accept": "text/plain"},
    files={"username": (None, username), "password": (None, password)},
)

if response.status_code == 200 and response.text.strip():
    token = response.text.strip()
    print("Got token:", token)
    with open("token.txt", "w") as f:
        f.write(token)
else:
    print(f"Failed to get token: {response.status_code} {response.text}")
    exit(1)
