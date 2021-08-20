#!/usr/bin/python3
"""2. POST an email #0  """

from sys import argv
import urllib.parse
import urllib.request

if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
