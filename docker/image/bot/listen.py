import websocket
from websocket._exceptions import WebSocketConnectionClosedException, WebSocketProtocolException
import requests
import json
import threading
import time
import os

discord_token = os.getenv('TOKEN')
bot_name = os.getenv('COMMAND')
guild_id = os.getenv('CLANID')
my_id = os.getenv('ME')
heartbeat_interval = int(os.getenv('HEARTBEAT'))
jenkins_api_token = '113e1b236004a8201fa31cc30ad92ff8c4'
discord_url = 'wss://gateway.discord.gg/?v=6&encording=json'

stop_threads = False

def wsConnect(ws):
    print('connecting to discord ...')
    disconnected = True
    while disconnected:
        try:
            ws.connect(discord_url)
            disconnected = False
        except Exception as e:
            print(e)
            time.sleep(2)
            pass
    print('discord connected ...')

def check_user_authorization(user_id, channel_id):
    header = {
        'authorization': discord_token
    }

    result = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}', headers=header)

    print(result.status_code)
    
    if result.status_code == 200:
        print(result.text)
        return True
    else:
        print('comando nao autorizado!!')
        os.system(f'python3 /bot/speak.py {channel_id} "opa tudo bem?? entaaao, eu dei uma checada nas tuas credenciais e n vo pode faze isso pra ti n, foi mal mesmo D:"')
        return False

def send_json_request(ws, request):
    try:
        ws.send(json.dumps(request))
    except WebSocketConnectionClosedException or WebSocketProtocolException as e:
        print('send_json_request error::', e)
        wsConnect(ws)
        ws.send(json.dumps(request))
        print('json sended ...')

def receive_json_response(ws):
    try:
        response = ws.recv()
        if response:
            return json.loads(response)
    except Exception as e:
        print('receive_json_response error::', e)
        wsConnect(ws)
        response = ws.recv()
        if response:
            print('json received')
            return json.loads(response)

def heartbeat(interval, ws):
    if stop_threads:
        exit()
    print(f'heartbeat begin with interval of {interval} sec.')
    while True:
        time.sleep(interval)
        heartbeatJson = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJson)
        print("hearbeat send")

def commandExecuteWParams(command, params, author_id, channel_id):
    os.system(f'curl -X POST -u admin:{jenkins_api_token} "localhost:8080/job/{command}/buildWithParameters?AUTHOR={author_id}&CHANNEL={channel_id}&{params}"')
    exit()

def commandExecuteWoutParams(command, author_id, channel_id):
    os.system(f'curl -X POST -u admin:{jenkins_api_token} "localhost:8080/job/{command}/buildWithParameters?AUTHOR={author_id}&CHANNEL={channel_id}"')
    exit()

def process_event(event, bol):
    command = event['d']['content'].split()
    if command[0] == bot_name:
        print(f"{event['d']['author']['username']}({event['d']['author']['id']}): {event['d']['content']}")
        if event['d']['author']['id'] != my_id and check_user_authorization(event['d']['author']['id'], event['d']['channel_id']):
            print('executando comando ....')
            if command[0] == bot_name:
                if len(command) > 2:
                    threading._start_new_thread(commandExecuteWParams, (command[1], command[2], event['d']['author']['id'], event['d']['channel_id']))
                else:
                    threading._start_new_thread(commandExecuteWoutParams, (command[1], event['d']['author']['id'], event['d']['channel_id']))

ws = websocket.WebSocket()
wsConnect(ws)
event = receive_json_response(ws)

threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

payload = {
    'op': 2,
    'd': {
        'token': discord_token,
        'properties': {
            '$os': 'windows',
            '$browser': 'chrome',
            '$device': 'pc'
        }
    }
}

send_json_request(ws, payload)

while True:
    try:
        event = receive_json_response(ws)
        if event['op'] == 11:
            print('heartbeat received')
        elif 'author' in event['d'] and 'content' in event['d']:
            threading._start_new_thread(process_event, (event, True))
    except Exception as e:
        print('main while loop error::', e)
        stop_threads = True
        pass 