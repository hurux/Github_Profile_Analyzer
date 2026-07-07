import requests
import time


def get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    return requests.get(url).json()


def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    return requests.get(url).json()


def calculate_repos(repos):
    repo_count = len(repos)

    if repo_count == 0:
        return {
            "repo_count": 0,
            "total_stars": 0,
            "total_forks": 0,
            "total_issues": 0,
            "top_repo": None,
            "languages": {},
            "most_used_language": None
        }

    total_stars = 0
    total_forks = 0
    total_issues = 0

    languages = {}
    top_repo = repos[0]

    for repo in repos:
        total_stars += repo['stargazers_count']
        total_forks += repo['forks_count']
        total_issues += repo['open_issues_count']

        if repo['stargazers_count'] > top_repo['stargazers_count']:
            top_repo = repo

        repo_language = repo['language']

        if repo_language is None:
            continue

        if repo_language in languages:
            languages[repo_language] += 1
        else:
            languages[repo_language] = 1

    most_used_language = max(languages, key=languages.get) if languages else None

    return {
        "repo_count": repo_count,
        "total_stars": total_stars,
        "total_forks": total_forks,
        "total_issues": total_issues,
        "top_repo": top_repo,
        "languages": languages,
        "most_used_language": most_used_language 
    }
