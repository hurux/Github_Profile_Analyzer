# GitHub Repository Analyzer

A lightweight Python application that utilizes the GitHub REST API to fetch data and calculate repository metrics for any given user.

## Features

- **Repository Count:** Calculates the total number of public repositories.
- **Engagement Metrics:** Sums up cumulative stats for total stars, forks, and open issues.
- **Top Performer:** Automatically detects the user's single most starred repository.
- **Language Analytics:** Tracks programming language frequency and isolates the most used language.
- **Safe Execution:** Robustly handles edge cases, such as users with empty profiles or missing language tags.

## Installation

Ensure you have Python installed, then set up the required dependency:

```bash
pip install requests
```

## Usage

Simply run the script within your Python environment:

```bash
python main.py
```
