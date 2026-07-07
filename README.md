# GitHub Repository & Profile Analyzer

A lightweight Python command-line application that utilizes the GitHub REST API to fetch user details and analyze repository metrics in real-time.

## Features

- **Interactive CLI Loop:** Runs continuously inside a `while` loop, allowing you to query multiple users one after another without restarting the application.
- **Profile Summary:** Fetches and displays essential user information including profile URL, name, bio, and follower/following counts.
- **Repository Metrics:** Calculates total public repositories, cumulative stars, forks, and open issues.
- **Language Analytics:** Breaks down language usage frequency across all projects and automatically identifies the user's most used language.
- **Robust Error Handling:** Seamlessly handles empty profiles, missing language tags, and non-existent usernames without crashing.

## Sample Output

```text
=== GitHub User Statistics Program ===
Type 'exit' to quit the program.

Enter GitHub Username: octocat

Fetching data for octocat...

========================================
 USER: The Octocat (@octocat)
========================================
Profile URL        : https://github.com
Followers / Lines  : 9500 Followers / 9 Following
Bio                : Testing out GitHub Spoons
----------------------------------------
Total Repositories : 8
Total Stars        : 1450
Total Forks        : 3200
Open Issues        : 12
Most Used Language : Ruby
Top Starred Repo   : Boysenberry-Repo (520 Stars)
Languages Used     :
  - Ruby: 4 repo(s)
  - HTML: 2 repo(s)
  - JavaScript: 2 repo(s)
========================================

Enter GitHub Username: exit
Closing the program...
```

## Installation

Ensure you have Python installed, then set up the required dependency:

```bash
pip install requests
```

## Usage

Simply run the script and enter any GitHub username when prompted. Type `exit` to close the application.
