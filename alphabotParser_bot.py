import discord, time
from alphabotParser import main


class MyClient(discord.Client):
    async def on_message(self,message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_ready(self):
        channel = self.get_channel(1027814569697087560)
        while True:
            try:
                await channel.send(main())
            except Exception:
                print('нет новых проектов,ждем')
                continue
            time.sleep(1)



client = MyClient()
client.run('MTAyNzgxNDg0MTE0NDA0OTY3NA.GvMFLq.nqLOPhoCwnZTbH_XkPkdaRdiN0HY0vYS0QblaM')
