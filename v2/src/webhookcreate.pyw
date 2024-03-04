import sys
import requests
import subprocess

if len(sys.argv) != 5:
    print("Usage: <bot_token> <channel_id> <message> <many_times>")
    sys.exit(1)
bot_token,channel_id,message,many_times = sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4])
create = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/webhooks",headers={"Authorization": f"Bot {bot_token}"},json={"name": "zufinho nuker v2","avatar": None})
print(create.json())
subprocess.Popen(['src/webhooksender.pyw', create.json().get('url'), message, str(many_times)], creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
print(create.status_code)
with open("result.log","a") as log:
    log.write(str(create.status_code))
    log.write("\n")