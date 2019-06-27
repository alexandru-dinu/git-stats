import github
import argparse
import os
from datetime import datetime

import json
from pprint import pprint

KEYS = ['forks_count', 'open_issues_count', 'stargazers_count', 'subscribers_count', 'watchers_count']

def collect(args):
    gh = github.GitHub(access_token=args.token)
    repo = gh.repos(args.org, args.repo)
    repo_info = repo.get()

    stats = {k: repo_info[k] for k in KEYS}
    traffic = repo.traffic.views.get()

    data = {**stats, **traffic}

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs(args.dir, exist_ok=True)

    fp = open(os.path.join(args.dir, f'{args.org}@{args.repo}@{timestamp}.json'), 'wt')
    json.dump(data, fp)
    fp.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--org', type=str, required=True)
    parser.add_argument('--repo', type=str, required=True)
    parser.add_argument('--token', type=str, required=True)
    parser.add_argument('--dir', type=str, default='history')
    args = parser.parse_args()

    collect(args)


if __name__ == "__main__":
    main()
