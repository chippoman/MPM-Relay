from telethon import TelegramClient
import discum
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Remember to use your own values from my.telegram.org!
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
client = TelegramClient('anon', api_id, api_hash)

bot = discum.Client(token=config['Discord']['token'])

async def main():
    async for message in client.iter_messages(-1001368873436, from_user='mining_pools_monitor_bot', limit=1, reverse=False):
        print(message.text)
        print(message.id)
        print(message.date)

        bot.sendMessage(config['Discord']['channel_id'], message.text)
   
with client:
    client.loop.run_until_complete(main())