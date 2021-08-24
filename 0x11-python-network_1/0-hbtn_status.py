#!/usr/bin/python3
"""0. What's my status? #0"""

import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    utf = the_page.decode("utf-8")
    print("Body response:")
    print("\t- type: {}".format(type(the_page)))
    print("\t- content: {}".format(the_page))
    print("\t- utf8 content: {}".format(utf))
