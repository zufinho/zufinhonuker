import requests
import sys
if len(sys.argv) != 4:
    print("Usage: <channel_id> <bot_token> <new_channel_name>")
    sys.exit(1)
channel_id, bot_token, new_channel_name = sys.argv[1], sys.argv[2], sys.argv[3]
api_url = f"https://discord.com/api/v9/channels/{channel_id}"
rename = requests.patch(api_url, headers={"Authorization": f"Bot {bot_token}","Content-Type": "application/json"}, json={"name": new_channel_name,})
print(rename.status_code,rename.text)
with open("result.log","a") as log:
    log.write(str(rename.status_code))
    log.write("\n")