import requests
import sys
import os
if len(sys.argv) != 5:
    ("Usage: <serverid> <token> <type of channel> <channel name>")
    sys.exit(1)
serverid=sys.argv[1]
token=sys.argv[2]
typechannel=int(sys.argv[3])
channelname=sys.argv[4]


api = f"https://discord.com/api/v9/guilds/{serverid}/channels"
headers = {
    "Authorization": f"Bot {token}",
    "Content-Type": "application/json",
}
payload = {
    "name": channelname,
    "type": typechannel, 
}
createchannel=requests.post(api, headers=headers, json=payload)
print(createchannel.status_code)
os.system(f"echo {createchannel} >> log.txt")