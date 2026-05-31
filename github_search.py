import requests

def search_github_repos(query):

    username = "Pranjali23d"

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    repos = response.json()

    results = []

    for repo in repos:

        repo_name = repo["name"]

        if query.lower() in repo_name.lower():
            results.append(repo_name)

    return results