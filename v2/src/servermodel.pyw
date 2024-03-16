import requests
import sys

if len(sys.argv) != 3:
    print("Usage: <guild_id> <bot_token>")
    sys.exit(1)
guild_id, bot_token = sys.argv[1], sys.argv[2]

# Obtém a lista de templates do servidor
verify = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/templates", headers={"Authorization": f"Bot {bot_token}"})

if verify.status_code == 200:
    templates = verify.json()
    if templates:
        for template in templates:
            delete_response = requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}/templates/{template['code']}", headers={"Authorization": f"Bot {bot_token}"})
            print("deleted",template['code'])
            if delete_response.status_code != 200:
                print(f"Erro ao deletar template: {template['code']}")
                sys.exit(1)
    # Obtém a lista de templates novamente para garantir que todas as templates sejam excluídas
    verify = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/templates", headers={"Authorization": f"Bot {bot_token}"})
    templates = verify.json()
    if templates:
        for template in templates:
            delete_response = requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}/templates/{template['code']}", headers={"Authorization": f"Bot {bot_token}"})
            if delete_response.status_code != 200:
                print(f"Erro ao deletar template: {template['code']}")
                sys.exit(1)
    # Cria um novo template
    clone = requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/templates", headers={"Authorization": f"Bot {bot_token}"}, json={"name": "zufinho nuker v2", "description": "zufinho nuker v2"})
    if clone.status_code == 200:
        with open("servermodel.txt", "w") as log:
            log.write(f"https://discord.new/{clone.json().get('code')}\n")
        with open("result.log", "a") as log:
            log.write(f"{clone.status_code}\n")
    else:
        print(clone.status_code, clone.text)
else:
    print(verify.status_code, verify.text)
    with open("servermodel.txt", "w") as log:
        log.write(f"error {verify.status_code}")
    sys.exit(1)

create_guild = requests.post(f"https://discord.com/api/v9/guilds", headers={"Authorization": f"Bot {bot_token}"}, json={"name": "zufinho nuker v2", "region": "brazil", "icon": None, "channels": None, "system_channel_id": None, "afk_channel_id": None, "afk_timeout": 300, "verification_level": 0, "default_message_notifications": 0, "explicit_content_filter": 0, "roles": None, "template_code": clone.json().get('code')})