#!/usr/bin/python3
"""3. Error code #0"""

from sys import argv
import urllib.request
import urllib.error

if __name__ == '__main__':
    url = argv[1]

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
