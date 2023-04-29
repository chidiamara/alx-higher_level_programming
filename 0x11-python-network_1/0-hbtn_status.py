#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == '__main__':
    r = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(r) as res:
        print("Body response:")
        html = res.read()
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))
