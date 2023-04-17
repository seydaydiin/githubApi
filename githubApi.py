import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'

    def getUser(self, username, auth_token):
        response = requests.get(f"{self.api_url}/users/{username}", headers={"Authorization": f"Token {auth_token}"})
        return response.json()

    def getRepositories(self, username, auth_token):
        response = requests.get(f"{self.api_url}/users/{username}/repos", headers={"Authorization": f"Token {auth_token}"})
        return response.json()

    def createRepository(self, name, token):
        headers = {'Authorization': f'token {token}'}
        payload = {
            'name': name,
            'auto_init': True,
            'private': False
        }
        response = requests.post(f'{self.api_url}/user/repos', headers=headers, json=payload)
        return response.json()

    """def createRepository(self, name, auth_token):
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Token {auth_token}"
        }
        data = {
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://seydaydiin.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }
        response = requests.post(f"{self.api_url}/user/repos", headers=headers, json=data)
        return response.json()"""

auth_token ='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'
github = Github()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            username= input('username: ')
            result = github.getUser(username, auth_token)
            print(f"name: {result['name']} public repos: {result['public_repos']}  follower : {result['followers']}")
        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username, auth_token)
            for repo in result:
                print(repo['name'])
        elif secim == '3':
            name = input('repository name: ')
            result = github.createRepository(name, auth_token)
            print(result)
        else:
            print('yanlış seçim')
