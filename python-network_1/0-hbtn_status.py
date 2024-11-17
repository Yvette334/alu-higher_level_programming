#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    body = response.read()

# Print the response body in the required format
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {body.decode('utf-8')}")
