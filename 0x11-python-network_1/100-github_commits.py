#!/usr/bin/python3
"""10. Time for an interview!"""

from sys import argv
import requests

if __name__ == '__main__':
    owner = argv[1]
    repository = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repository)
    values = {'sort': 'created', 'per_page': 10}
    req = requests.get(url, params=values)
    try:
        response = req.json()
        if len(response) > 0:
            for item in response:
                print("{}: {}".format(
                    item['sha'], item['commit']['author']['name']))
        else:
            print("No result")
    except:
        pass
