from telethon import TelegramClient
import discum
import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')
cwd = os.path.dirname(os.path.realpath('__file__'))
sessionStorage = os.path.join(cwd, 'anon.session')

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
client = TelegramClient(sessionStorage, api_id, api_hash)

async def main():
    async for message in client.iter_messages(-1001368873436, from_user='mining_pools_monitor_bot', limit=1, reverse=False):
        last_id = config['Telegram']['last_id']

        if (message.id > int(last_id) and "eth pool" in message.text):
            bot = discum.Client(token=config['Discord']['token'])
            config['Telegram']['last_id'] = str(message.id)
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            bot.sendMessage(config['Discord']['channel_id'], message.text)
   
with client:
    client.loop.run_until_complete(main())