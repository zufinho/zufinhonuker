import requests
import sys
if len(sys.argv) != 5:
    print("Usage: <guild_id> <bot_token> <role_id> <new_role_name>")
    sys.exit(1)
guild_id, bot_token, role_id, new_role_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
rename = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}", headers={"Authorization": f"Bot {bot_token}","Content-Type": "application/json",}, json={"name": new_role_name,})
print(rename.status_code,rename.text)
with open("result.log","a") as log:
    log.write(str(rename.status_code))
    log.write("\n")