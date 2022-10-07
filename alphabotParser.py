import fake_useragent, requests

projects_list_ids = []
print('program started')  
user_agent = fake_useragent.UserAgent().random
headers = {
    "User-Agent": user_agent
}
url = "https://www.alphabot.app/api/projects?sort=startDate&scope=all&sortDir=-1&showHidden=true&pageSize=16&pageNum=0&search="

def main():
    if len(projects_list_ids) > 500:
        projects_list_ids.clear()
    req = requests.get(url, headers=headers)
    projects = req.json()
    for project in reversed(projects):
        if project['_id'] not in projects_list_ids:
            projects_list_ids.append(project["_id"])
            project_url = "https://www.alphabot.app/"+ project['slug']
            name = project['name']
            res = f'----------------------------\n{name}\n{project_url}'
            return res
if __name__ == '__main__':
    main()
