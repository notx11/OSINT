#! /usr/bin/python

import requests, getopt, sys

def usage():
    sys.stderr.write ("Usage: " + sys.argv[0] + " [options]\n")
    sys.stderr.write ("  -u <userid>           Social Media Handle\n")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'u:h', ['userid=','help='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    userid = None
    for o, a in opts:
        if o in ("-u", "--user"):
            userid = a
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)

    websites = ["https://www.instagram.com/", "https://twitter.com/", "http://pastebin.com/u/", "https://www.reddit.com/user/", "https://github.com/"]
    username = userid

    for website in websites:
        url = website + username

        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
                print "[*] User exists here: " + url
        else:
                print "[!] User NOT FOUND here: " + url

if __name__ == '__main__':
    main()
