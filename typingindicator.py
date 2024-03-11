import requests
import time
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()

with open(".env", "r") as file:
    info = file.read().splitlines()

def configure_token():
    try:
        token = input("Discord token: ")
        with open(".env", "w") as file:
            file.write(f"TOKEN = {token}")
    except Exception as e:
        print(f"Error configuring Discord token{e}")
        exit()

def configure_channel():
    global channel_id
    channel_id = input("Channel ID: ")

def send_typing():
    r = requests.post("https://discord.com/api/v9/channels/" + channel_id + "/typing", headers=header)
    time.sleep(5)

def start_typing():
    while 1 == 1:
        send_typing()

if (len(os.getenv("TOKEN"))):
    print("Missing token! Attempting to reconfigure...")
    time.sleep(2)
    configure_token()
    time.sleep(1)
    with open(".env", "r") as file:
        info = file.read().splitlines()
    print("Successfully configured!")

token = os.getenv("TOKEN")

header = {
    'authorization': token
}

configure_channel()
print("Started typing indicator! Press CTRL+C to stop.")
start_typing()