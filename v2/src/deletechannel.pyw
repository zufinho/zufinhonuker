import sys
import requests
if len(sys.argv) != 4:
    print("Usage: <bot_token> <channel_id>")
token, channel_id = sys.argv[1], sys.argv[2]
delete = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers={"Authorization": f"Bot {token}",})
print(delete.status_code,delete.text)
with open("result.log","a") as log:
    log.write(str(delete.status_code))
    log.write("\n")