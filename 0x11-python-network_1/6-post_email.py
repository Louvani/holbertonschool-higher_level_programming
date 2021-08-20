#!/usr/bin/python3
"""6. POST an email #1 """

from sys import argv
import requests

if __name__ == '__main__':
    url = argv[1]
    value = {'email': argv[2]}

    req = requests.post(url, data=value)
    print(req.text)
