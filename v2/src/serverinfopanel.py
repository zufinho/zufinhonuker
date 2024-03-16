import requests
from pystyle import Colorate, Colors
import time
import sys
import os
if len(sys.argv) != 3:
    print("Usage: script.py <guild_id> <bot_token>")
    sys.exit(1)
def printcolor(text):
    print(Colorate.Horizontal(Colors.purple_to_blue,text,1))
guild_id, bot_token = sys.argv[1], sys.argv[2]
HEADERS = {'Authorization': f'Bot {bot_token}'}
response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers=HEADERS)
verification_levels = {
    0: "None",
    1: "Low - Email verified",
    2: "Medium - Registered on Discord for more than 5 minutes",
    3: "High - Member of the server for more than 10 minutes",
    4: "Highest - Phone verified"
}
level = response.json().get('verification_level')
level_text = verification_levels.get(level, "Unknown")
while True:
    response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}?with_counts=true', headers=HEADERS)
    if response.status_code == 200:
        guild_info = response.json()
        printcolor(f"Server Name: {guild_info['name']}")
        printcolor(f"Server Owner: {requests.get(f'https://discord.com/api/v9/users/{guild_info['owner_id']}',headers=HEADERS).json()['username']}")
        printcolor(f"Server Owner id: {guild_info['owner_id']}")
        printcolor(f"Members Count: {guild_info['approximate_member_count']}")
        printcolor(f"Emoji Count: {len(guild_info.get('emojis', []))}")
        printcolor(f"Roles Count: {len(guild_info.get('roles', []))}")
        printcolor(f"Verification Level: {level_text}")

        channels_url = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
        response = requests.get(channels_url, headers=HEADERS)
        if response.status_code == 200:
            channels = response.json()
            printcolor(f"Channels Count: {len(channels)}")
        else:
            print("Error at obtain server info:", response.status_code, response.text)

        bans_url = f'https://discord.com/api/v9/guilds/{guild_id}/bans'
        response = requests.get(bans_url, headers=HEADERS)
        if response.status_code == 200:
            bans_info = response.json()
            printcolor(f"Banned Members Count: {len(bans_info)}")
        else:
            print(f"Error at obtain server bans: {response.status_code, response.text}")
    else:
        print(f"Error at obtain server info: {response.status_code, response.text}")

    time.sleep(10)
    os.system("cls")
