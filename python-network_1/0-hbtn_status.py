#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    urls = [
        "https://intranet.hbtn.io/status",
        "http://0.0.0.0:5050/status"
    ]

    for url in urls:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
