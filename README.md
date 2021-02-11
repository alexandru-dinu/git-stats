# GitHub statistics

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Simple script using [PyGithub](https://pygithub.readthedocs.io/en/latest/introduction.html#) to fetch statistics about the repositories of an user or an organization.


## Usage

```bash
usage: main.py [-h] --token TOKEN [--org ORG] [--fork_only]

optional arguments:
  -h, --help     show this help message and exit
  --token TOKEN  Path to a file containing GitHub access token.
  --org ORG      Username or organization.
  --fork_only    Inspect only forks.
```
