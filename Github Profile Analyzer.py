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

if __name__ == "__main__":
    print("=== GitHub User Statistics Program ===")
    print("Type 'exit' to quit the program.\n")

    while True:
        username = input("Enter your username : ").strip()

        if username.lower() == "exit":
            print("Closing the program.")
            break

        if not username:
            print("Please enter a valid username.\n")
            continue

        print(f"\nFetching data for {username}...")

        user_data = get_user_data(username)

        if user_data.get('message') == "Not Found":
            print("Error: User not found! Please try again.\n")
            continue

        repos_data = get_repos(username)
        if not isinstance(repos_data, list):
            print("Error: Could not retrieve repositories.\n")
            continue

        stats = calculate_repos(repos_data)

        print("\n" + "="*40)
        print(f" USER: {user_data.get('name') or username} (@{username})")
        print("="*40)
        print(f"Profile URL        : {user_data.get('html_url')}")
        print(f"Followers / Lines  : {user_data.get('followers')} Followers / {user_data.get('following')} Following")
        print(f"Bio                : {user_data.get('bio') or 'No bio available'}")
        print("-"*40)
        print(f"Total Repositories : {stats['repo_count']}")
        print(f"Total Stars        : {stats['total_stars']}")
        print(f"Total Forks        : {stats['total_forks']}")
        print(f"Open Issues        : {stats['total_issues']}")
        print(f"Most Used Language : {stats['most_used_language'] or 'Unknown'}")
        
        if stats['top_repo']:
            print(f"Top Starred Repo   : {stats['top_repo']['name']} ({stats['top_repo']['stargazers_count']} Stars)")
        else:
            print("Top Starred Repo   : None")
            
        print("Languages Used     :")
        if stats['languages']:
            for lang, count in stats['languages'].items():
                print(f"  - {lang}: {count} repo(s)")
        else:
            print("  - No language data found.")
        print("="*40 + "\n")

        time.sleep(1)
