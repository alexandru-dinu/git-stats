import argparse
from pathlib import Path
from collections import namedtuple

from github import Github


def _get_gh(token: Path) -> Github:
    with open(token, 'rt') as fp:
        tk = fp.read().strip()

    return Github(tk)


def list_all_repos(args) -> None:
    gh = _get_gh(Path(args.token))

    attrs = ['name', 'created_at', 'fork', 'git_url']
    Repo = namedtuple('Repo', attrs)

    data = []
    for repo in gh.get_user().get_repos():
        data.append(Repo(*[getattr(repo, attr) for attr in attrs]))

    data = sorted(data, key=lambda r: r.created_at)
    data = filter(lambda r: args.org in r.git_url, data)

    if args.fork_only:
        data = filter(lambda r: r.fork, data)

    for repo in data:
        s = f'{repo.name:40s} @ {str(repo.created_at):20s}'
        if repo.fork:
            s += ' (fork)'
        print(s)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--token', type=str, required=True,
            help='Path to a file containing GitHub access token.')
    parser.add_argument('--org', type=str, required=False,
            help='Username or organization.')
    parser.add_argument('--fork_only', action='store_true',
            help='Inspect only forks.')

    args = parser.parse_args()

    list_all_repos(args)


if __name__ == "__main__":
    main()
