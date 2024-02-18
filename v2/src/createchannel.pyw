import requests
import sys
if len(sys.argv) != 5:
    print("Usage: <guild_id> <bot_token> <type of channel> <channel name>")
    sys.exit(1)
guild_id,bot_token,typechannel,channelname=sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
createchannel=requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers={"Authorization": f"Bot {bot_token}","Content-Type": "application/json",}, json={"name": channelname, "type": typechannel})
print(createchannel.status_code,createchannel.text)
with open("result.log","a") as log:
    log.write(str(createchannel.status_code))
    log.write("\n")