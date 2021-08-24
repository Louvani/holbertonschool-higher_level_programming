#!/usr/bin/python3
"""3. Error code #0"""

from sys import argv
import requests

if __name__ == '__main__':
    url = argv[1]

    r = requests.get(url)
    status = r.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(r.text)
