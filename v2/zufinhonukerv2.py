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
#color classes
class printcolor():
    def default(text):
        print(Colorate.Horizontal(Colors.purple_to_blue,text,1))
guildverified=0
while True:
    os.system("cls")
    printcolor.default(banner)
    print()
    print()
    printcolor.default(version)
    print()
    printcolor.default("Digit the token bot:")
    token=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
    #verify if bot token is valid
    tokenverify = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f"Bot {token}"})
    if tokenverify.status_code==200:
        while True:
            os.system("cls")
            printcolor.default(banner)
            print()
            print()
            printcolor.default(version)
            print()
            printcolor.default("Digit the guild id:")
            guildid=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
            #verify if bot in guild
            guildverify=requests.get("https://discord.com/api/v9/users/@me/guilds", headers={"Authorization": f"Bot {token}"})
            for guild in guildverify.json():
                if guild['id']==guildid:
                    guildverified=1
                    break
            else:
                printcolor.default("Bot not is in guild")
                time.sleep(3)
            if guildverified==1:
                break
    else:
        printcolor.default("insert a valid token")
        time.sleep(3)
    if guildverified==1:
        break
#all ok
