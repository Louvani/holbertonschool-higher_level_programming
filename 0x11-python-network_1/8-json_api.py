#!/usr/bin/python3
"""8. Search API"""

from sys import argv
import requests

if __name__ == '__main__':
    values = {}
    if len(argv) > 1:
        values['q'] = argv[1]
    else:
        values['q'] = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data=values)

    try:
        response = req.json()
        if len(response) > 0:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
