import requests
import sys

if len(sys.argv) != 4:
    print("Usage: <channel_id> <bot_token> <new_channel_name>")
    sys.exit(1)

channel_id, bot_token, new_channel_name = sys.argv[1], sys.argv[2], sys.argv[3]

api_url = f"https://discord.com/api/v9/channels/{channel_id}"
headers = {
    "Authorization": f"Bot {bot_token}",
    "Content-Type": "application/json",
}
payload = {
    "name": new_channel_name,
}

response = requests.patch(api_url, headers=headers, json=payload)

print(response.status_code)