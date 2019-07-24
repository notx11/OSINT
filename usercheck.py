#!/usr/bin/env python

import argparse
from __future__ import print_function
import logging
import requests

WEBSITES = [
    "https://www.instagram.com/{}/media/",
    "https://twitter.com/{}",
    "http://pastebin.com/u/{}",
    "https://www.reddit.com/user/{}.json", # use .json for reddit to avoid rate limiting and stuff
    "https://github.com/{}"
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--userid", required=True, help="Social Media Handle")
    parser.add_argument("-d", "--debug", action="store_true", help="Prints Debug from API Call")
    args = parser.parse_args()

    username = args.userid
    session = requests.session()
    session.headers['User-agent'] = 'uiuc-tsprivsec.usercheck:0.9'

    for website in WEBSITES:
        url = website.format(username)

        # use custom user agent because reddit wants bots to use them
        response = session.get(url, allow_redirects=False)
        if response.status_code == 200:
                print("[*] User exists here: " + url)
        else:
                print("[!] User NOT FOUND here: " + url)

if __name__ == '__main__':
    main()
