import requests
import sys
if len(sys.argv) != 5:
    print("Usage: <guild_id> <bot_token> <member_id> <ban_reason>")
    sys.exit(1)
guild_id,bot_token,member_id,ban_reason = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
ban=requests.put(f'https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}',headers={'Authorization': f'Bot {bot_token}','Content-Type': 'application/json',},json={'delete_message_days': '0','reason': ban_reason,})
print(ban.status_code,ban.text)
with open("result.log","a") as log:
    log.write(str(ban.status_code))
    log.write("\n")