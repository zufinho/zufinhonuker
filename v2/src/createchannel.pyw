import requests
import sys
if len(sys.argv) != 5:
    ("Usage: <serverid> <token> <type of channel> <channel name>")
    sys.exit(1)
serverid,token,typechannel,channelname=sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]


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
