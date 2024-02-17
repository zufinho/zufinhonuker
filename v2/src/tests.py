#isso é um arquivo de tests, para depois ser implementado no programa
#pegar id dos canais
import requests
import os

token = "MTE5ODQ2MTUyMzg5OTcxMTU5OQ.GDhl6y.ZedeHj1A802s92nZog01VS8WB4GEZ6tFkPLpkw"  # Substitua pelo seu token de bot real
guild_id = "1208525411714072676"  # Substitua pelo ID do servidor

url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
headers = {
    "Authorization": f"Bot {token}",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    channels = response.json()
    for channel in channels:
        print(f"ID: {channel['id']} - Nome: {channel['name']}")
        os.system(f"start src/functions/deletechannel.pyw {token} {channel['id']}")

else:
    print(f"Erro ao buscar canais: {response.status_code} - {response.text}")

#///////////////////////////