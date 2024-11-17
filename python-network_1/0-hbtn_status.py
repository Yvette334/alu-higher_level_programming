#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    request = urllib.request.Request(url)
    
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))  # Expected: <class 'bytes'>
            print("\t- content: {}".format(body))    # Expected: b'OK'
            print("\t- utf8 content: {}".format(body.decode("utf-8")))  # Expected: OK
    except urllib.error.URLError as e:
        print(f"Error: {e}")
