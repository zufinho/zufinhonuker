import sys
import requests
if len(sys.argv) != 4:
    print("Usage: <token> <channel_id>")
token = sys.argv[1]
channel_id = sys.argv[2]

# Configura os headers da requisição
headers = {
    "Authorization": f"Bot {token}",
}

# URL da API para deletar o canal
api = f"https://discord.com/api/v9/channels/{channel_id}"

# Faz a requisição DELETE para a API do Discord
response = requests.delete(api, headers=headers)

# Verifica se o canal foi deletado com sucesso
if response.status_code == 204:
    print("Canal deletado com sucesso.")
else:
    print(f"Erro ao deletar canal: {response.status_code} - {response.text}")
