import requests
import sys
if len(sys.argv) != 5:
    print("Usage: <guild_id> <bot_token> <user_id> <new_nickname>")
    sys.exit(1)
guild_id, bot_token, user_id, new_nickname = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
changenick = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}", headers={"Authorization": f"Bot {bot_token}","Content-Type": "application/json",}, json={"nick": new_nickname,})
print(changenick.status_code,changenick.text)
with open("result.log","a") as log:
    log.write(str(changenick.status_code))
    log.write("\n")