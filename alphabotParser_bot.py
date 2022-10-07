import discord, time
from alphabotParser import main


class MyClient(discord.Client):
    async def on_message(self,message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_ready(self):
        channel = self.get_channel(YOUR_CHANNEL_ID_WITHOUT_BRACKETS)
        while True:
            try:
                await channel.send(main())
            except Exception:
                continue
            time.sleep(1)



client = MyClient()
client.run('YOUR_TOKEN')
