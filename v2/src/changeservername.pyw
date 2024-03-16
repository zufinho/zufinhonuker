import sys
import requests
if len(sys.argv) !=4:
    print("Usage: <guild_id> <bot_token> <new_name_server>")
guild_id, bot_token, new_name_server = sys.argv[1],sys.argv[2],sys.argv[3]
changename = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}", headers={"Authorization": f"Bot {bot_token}", "Content-Type": "application/json"}, json={"name": new_name_server})
print(changename.status_code,changename.text)
with open("result.log","a") as log:
    log.write(str(changename.status_code))
    log.write("\n")