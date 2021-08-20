#!/usr/bin/python3
"""9. My GitHub!"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    user = argv[1]
    pwd = argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=HTTPBasicAuth(user, pwd))
    try:
        response = req.json()
        if len(response) > 0:
            print("{}".format(response['id']))
        else:
            print("No result")
    except:
        print("None")
