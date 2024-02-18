import sys
import requests
if len(sys.argv) != 4:
    print("Usage: <token> <channel_id>")
token, channel_id = sys.argv[1], sys.argv[2]

headers = {
    "Authorization": f"Bot {token}",
}

api = f"https://discord.com/api/v9/channels/{channel_id}"

delete = requests.delete(api, headers=headers)
