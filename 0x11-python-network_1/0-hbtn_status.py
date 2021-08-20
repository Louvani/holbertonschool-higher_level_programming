#!/usr/bin/python3
"""0. What's my status? #0"""

import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    utf = the_page.decode("utf-8")
    print("""Body response:\n\
        - type: {}
        - content: {}
        - utf8 content: {}""".format(type(the_page), the_page, utf))
