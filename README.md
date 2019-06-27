# GitHub statistics

Simple script using [GitHub API](https://pypi.org/project/githubpy/) to fetch statistics about user / organization repositories.

Running the script will produce a `json` file for the given org/repo containing traffic and counter info (forks, open issues, stargazers, subscribers, watchers).

```bash
python main.py
    --token TOKEN   # github access token
    --org USER/ORG  # user or organization name
    --repo REPO     # repository name
    [--dir DIR]     # directory to save json files (default = ./history)
```

Pretty printing can be done with

```bash
python -m json.tool JSON
```
