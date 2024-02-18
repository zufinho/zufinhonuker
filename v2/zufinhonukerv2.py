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
version="alpha 1.0 - v2"
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
    printcolor("[1] Create Channels         [2] Delete Channels")
    cmd=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
    if cmd=="1":
        #create channels
        printcolor("Name of channel")
        channelname=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        printcolor("Channel type:")
        printcolor("text/voice/category")
        channeltype=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
        if channeltype.lower()=="text":
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
        if cango==1:
            printcolor("Amount of channels:")
            amountchannels=int(input(Colorate.Horizontal(Colors.purple_to_blue,">",1)))

            #action
            print(channeltype)
            while count<=amountchannels:
                os.system(f"start src/createchannel.pyw {guildid} {token} {channeltype} {channelname}")
                printcolor(f"requested to create {channelname}")
                count=count+1
    elif cmd=="2":
        #delete channels

        #get channels ids and delete then
        guildapichannels = f"https://discord.com/api/v9/guilds/{guildid}/channels"
        headers = {
            "Authorization": f"Bot {token}",
        }

        response = requests.get(guildapichannels, headers=headers)

        if response.status_code == 200:
            channels = response.json()
            for channel in channels:
                printcolor(f"requested to delete {channel['name']}")
                os.system(f"start src/deletechannel.pyw {token} {channel['id']}")

        else:
            print(Colorate.Color(Colors.red,f"Error at search channels: {response.status_code} - {response.text}",1))