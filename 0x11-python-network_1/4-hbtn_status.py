#!/usr/bin/python3
"""3. Error code #0"""

import urllib.request

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode("utf-8")
    print("Body response:")
    print("\t- type: {}".format(type(the_page)))
    print("\t- content: {}".format(the_page))
