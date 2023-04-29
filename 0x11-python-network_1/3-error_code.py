#!/usr/bin/python3
"""
a Python script that takes in a URL, sendss a request to the URL
and displays the body of the response(decoded in utf8)
"""

import urllib.request
import sys

if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
