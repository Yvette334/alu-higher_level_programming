#!/usr/bin/python3
"""Fetches http://0.0.0.0:5050/status."""
import requests

if __name__ == "__main__":
    # Use the updated URL
    r = requests.get("http://0.0.0.0:5050/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
