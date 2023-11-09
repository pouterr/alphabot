import discord, time,asyncio, fake_useragent, requests

intents = discord.Intents.default()
projects_list_ids = []
print('program started')  
user_agent = fake_useragent.UserAgent().random
headers = {
    "User-Agent": user_agent
}
url = "https://www.alphabot.app/api/projects?sort=startDate&scope=all&sortDir=-1&showHidden=true&pageSize=16&pageNum=0&search="

async def main():
        if len(projects_list_ids) > 500:
            projects_list_ids.clear()
        req = requests.get(url, headers=headers)
        projects = await req.json()
        for project in reversed(projects):
            if project['_id'] not in projects_list_ids and project['type'] == 'fcfs':
                projects_list_ids.append(project["_id"])
                project_url = "https://www.alphabot.app/"+ project['slug']
                name = project['name']
                res = f'----------------------------\n{name}\n{project_url}'
                return res

class MyClient(discord.Client):
    async def on_message(self,message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_ready(self):
        channel = self.get_channel(1027814569697087560)
        while True:
            print('Делаю запрос...')
            try:
                await channel.send(await main())
            except Exception:
                print('Ничего нет(')
                time.sleep(3)
                continue
            await asyncio.sleep(5)



client = MyClient(intents=intents)
client.run('MTAyNzgxNDg0MTE0NDA0OTY3NA.GOKGkA.M_k6ZsfvSyCNrRAj86RCXA6AwygvsDMieziYuQ')