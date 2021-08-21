#!/usr/bin/python3
"""10. Time for an interview!"""

from sys import argv
import requests

if __name__ == '__main__':
    repository = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repository)
    values = {'per_page': 10}
    req = requests.get(url, params=values)
    try:
        response = req.json()
        for item in response:
            print("{}: {}".format(
                item['sha'], item['commit']['author']['name']))
    except IndexError:
        pass
