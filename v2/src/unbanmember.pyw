import requests
import sys
if len(sys.argv) != 4:
    print("Usage: <guild_id> <bot_token> <member_id>")
    sys.exit(1)
guild_id,bot_token,member_id = sys.argv[1],sys.argv[2],sys.argv[3]
unban=requests.delete(f'https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}',headers={'Authorization': f'Bot {bot_token}'})
print(unban.status_code, unban.text)
with open("result.log","a") as log:
    log.write(str(unban.status_code))
    log.write("\n")