import requests
import sys
if len(sys.argv) != 4:
    print("Usage: <guild_id> <bot_token> <member_id>")
    sys.exit(1)
guild_id,bot_token,member_id = sys.argv[1],sys.argv[2],sys.argv[3]
kick=requests.delete(f'https://discord.com/api/v9/guilds/{guild_id}/members/{member_id}',headers={'Authorization': f'Bot {bot_token}','Content-Type': 'application/json',})
print(kick.status_code)