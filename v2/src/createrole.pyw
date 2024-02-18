import requests
import sys

if len(sys.argv) != 4:
    print("Usage: <guild_id> <bot_token> <role_name>")
    sys.exit(1)
guild_id, bot_token, role_name= sys.argv[1], sys.argv[2], sys.argv[3]
api_url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
headers = {
    "Authorization": f"Bot {bot_token}",
    "Content-Type": "application/json",
}
cor_hex = "7014ba"
payload = {
    "name": role_name,
    "color": int(cor_hex, 16),
    "permissions": "0",
    "hoist": False,
    "mentionable": False
}
create = requests.post(api_url, headers=headers, json=payload)
print(create.status_code,create.text)
with open("result.log","a") as log:
    log.write(str(create.status_code))
    log.write("\n")