#!/usr/bin/env python3

import argparse
import requests

# Create argument parser
parser = argparse.ArgumentParser(prog='pyCurl', description='Simple HTTP client')
parser.add_argument('-U', '--user-agent', help='Specify User-Agent')
parser.add_argument('-R', '--redirect', help='Follow Redirects', action='store_true')
parser.add_argument('url', help='URL to make a request to')

# Parse the arguments
args = parser.parse_args()

url = args.url
headers = {}

# Check if the URL starts with a scheme (http:// or https://)
if not url.startswith("http://") and not url.startswith("https://"):
    url = "http://" + url

if args.user_agent:
    headers['User-Agent'] = args.user_agent
else:
    headers['User-Agent'] = 'pyCurl/1.0'  # Default user-agent value

try:
    response = requests.get(url, headers=headers, allow_redirects=args.redirect)

    # Print response status code
    print('Status code:', response.status_code)

    # Print response headers
    print('Headers:')
    for name, value in response.headers.items():
        print(f'{name}: {value}')

    # Print response body
    print('Body:')
    print(response.text)
except:
    print("No Response")