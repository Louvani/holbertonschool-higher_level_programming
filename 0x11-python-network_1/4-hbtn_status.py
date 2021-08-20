#!/usr/bin/python3
"""3. Error code #0"""

from sys import argv
import urllib.request
import urllib.error

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
