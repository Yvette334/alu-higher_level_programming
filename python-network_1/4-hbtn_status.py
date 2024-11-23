#!/usr/bin/python3
"""Fetches from both http://0.0.0.0:5050/status and https://intranet.hbtn.io/status."""
import requests

def fetch_url(url):
    """Fetch a URL and print its body response."""
    try:
        # Fetch the URL
        r = requests.get(url)
        print(f"Fetching {url}")
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
    except requests.exceptions.RequestException as e:
        # Handle exceptions and print the error
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    # Fetch from both URLs
    fetch_url("http://0.0.0.0:5050/status")  # For the local web server
    fetch_url("https://intranet.hbtn.io/status")  # For the external web server

