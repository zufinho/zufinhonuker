import requests
import sys

if len(sys.argv) != 3:
    print("Usage: <bot_token> <channel_id>")
    sys.exit(1)
bot_token,channel_id=sys.argv[1],sys.argv[2]
create = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/invites', json={'max_age': 0,'max_uses': 0}, headers={'Authorization': f'Bot {bot_token}'})
print(create.status_code,create.text)
with open("result.log","a") as log:
    log.write(str(create.status_code))
    log.write("\n")