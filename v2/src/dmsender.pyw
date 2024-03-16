import requests
import sys
if len(sys.argv) != 5:
    print("Usage: <bot_token> <user_id> <message> <loop>")
    sys.exit()
bot_token,user_id,message,loop=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]


createdm = requests.post('https://discord.com/api/v9/users/@me/channels', headers={'Authorization': f'Bot {bot_token}','Content-Type': 'application/json'}, json={'recipient_id': user_id})
if createdm.status_code == 200:
    createdm.json()['id']
else:
    print(createdm.status_code,createdm.text)
senddm = requests.post(f'https://discord.com/api/v9/channels/{createdm.json()['id']}/messages', headers={'Authorization': f'Bot {bot_token}','Content-Type': 'application/json'}, json={'content': message})
if senddm.status_code == 200:
    print()
else:
    print(senddm.status_code,senddm.text)
if loop==0:
    with open("result.log","a") as log:
        log.write(str(senddm.status_code))
        log.write("\n")

