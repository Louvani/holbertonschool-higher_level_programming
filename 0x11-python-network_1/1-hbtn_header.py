#!/usr/bin/python3
"""1. Response header value #0 """

import urllib.request
from sys import argv

if __name__ == '__main__':
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])
