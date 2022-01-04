import requests
import sys
import os

discord_token = os.getenv('TOKEN')
channel_id = sys.argv[1]
message = sys.argv[2]

payload = {
    'content': f'🤖 **Bot:** *{message}*'
}

header = {
    'authorization': discord_token
}

r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data=payload, headers=header)