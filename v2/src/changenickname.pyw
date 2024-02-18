import requests
import sys

if len(sys.argv) != 5:
    print("Usage: <guild_id> <bot_token> <user_id> <new_nickname>")
    sys.exit(1)

guild_id, bot_token, user_id, new_nickname = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

api_url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
headers = {
    "Authorization": f"Bot {bot_token}",
    "Content-Type": "application/json",
}
payload = {
    "nick": new_nickname,
}

response = requests.patch(api_url, headers=headers, json=payload)
print(response.status_code)
