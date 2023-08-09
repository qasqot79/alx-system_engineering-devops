#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers """
    username = 'qasqot79'
    password = 'Akanke79'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/qasqot79 API Python for Alx programming'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return(0)
