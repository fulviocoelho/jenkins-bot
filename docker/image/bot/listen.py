import websocket
import requests
import json
import threading
import time
import os
from datetime import datetime

discord_token = os.getenv('TOKEN')
bot_command = os.getenv('COMMAND')
guild_id = os.getenv('CLANID')
my_id = os.getenv('ME')
jenkins_api_token = '113e1b236004a8201fa31cc30ad92ff8c4'
discord_url = 'wss://gateway.discord.gg/?v=6&encording=json'
debug = bool(str(os.getenv('DEBUGLOG')) in ['true']) | False

debug_log = True
regular_log = False

def log(is_debug, *args):
    if debug == True:
        print(datetime.now().time(), *args)
    elif debug == False and is_debug == False:
        print(datetime.now().time(), *args)

def wsConnect(ws):
    ws.connect(discord_url)
    event = receive_json_response(ws)
    heartbeat_interval = int(event['d']['heartbeat_interval'] / 1000)
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
    log(regular_log, 'CONNECTED', event)

def check_user_authorization(user_id, channel_id):
    header = {
        'authorization': discord_token
    }

    result = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}', headers=header)

    log(debug_log, result.status_code)
    
    if result.status_code == 200:
        log(debug_log, result.text)
        return True
    else:
        log(regular_log, 'UNAUTHORIZED COMMAND!!')
        os.system(f'python3 /bot/speak.py {channel_id} "opa tudo bem?? entaaao, eu dei uma checada nas tuas credenciais e n vo pode faze isso pra ti n, foi mal mesmo D:"')
        return False

def send_json_request(ws, request):
    ws.send(json.dumps(request))
    
def receive_json_response(ws):
    response = ws.recv().encode('utf-8')
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    log(regular_log, f'BEGIN HEARBEAT WITH {interval} SEC. OF INTERVAL')
    try:
        while True:
            time.sleep(interval)
            heartbeatJson = {
                "op": 1,
                "d": "null"
            }
            send_json_request(ws, heartbeatJson)
            log(debug_log, "HEARTBEAT::: sended")
    except Exception as e:
        exit()

def commandExecuteWParams(command, params, author_id, channel_id):
    os.system(f'curl -X POST -u admin:{jenkins_api_token} "localhost:8080/job/{command}/buildWithParameters?AUTHOR={author_id}&CHANNEL={channel_id}&{params}"')
    exit()

def commandExecuteWoutParams(command, author_id, channel_id):
    os.system(f'curl -X POST -u admin:{jenkins_api_token} "localhost:8080/job/{command}/buildWithParameters?AUTHOR={author_id}&CHANNEL={channel_id}"')
    exit()

def process_event(event, bol):
    command = event['d']['content'].split()
    if len(command) <= 0:
        exit()
    elif command[0] == bot_command:
        log(regular_log, f"{event['d']['author']['username']}({event['d']['author']['id']}): {event['d']['content']}")
        if event['d']['author']['id'] != my_id and check_user_authorization(event['d']['author']['id'], event['d']['channel_id']):
            log(debug_log, 'executando comando ....')
            if len(command) > 2:
                threading._start_new_thread(commandExecuteWParams, (command[1], command[2], event['d']['author']['id'], event['d']['channel_id']))
            else:
                threading._start_new_thread(commandExecuteWoutParams, (command[1], event['d']['author']['id'], event['d']['channel_id']))

def main(ws):
    while True:
        try:
            event = receive_json_response(ws)
            if event is None or 't' not in event:
                pass
            log(debug_log, 'EVENT TYPE:::', event['t'])
            if event['t'] == 'MESSAGE_CREATE':
                if 'author' in event['d'] and 'content' in event['d']:
                    log(debug_log, event['d']['author']['username'])
                    threading._start_new_thread(process_event, (event, True))
            elif event['op'] == 11:
                log(debug_log, 'HEARTBEAT::: received')
        except Exception as e:
            if ws.connected == False:
                exit()
            else:
                log(debug_log, e)
            pass 

ws = websocket.WebSocket()

while True:
    try:
        main(ws)
    except:
        if ws.connected == False:
            try:
                wsConnect(ws)
            except Exception as e:
                log(debug_log, e)
                time.sleep(10)
        pass