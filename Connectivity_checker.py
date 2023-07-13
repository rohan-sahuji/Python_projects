# Program to check connectivity of site

import urllib.request as urllib

def conn_check(url):
    print('Checking connectivity...')
    response = urllib.urlopen(url)
    print('Successfully connectted to', url, 'with response code:', response.getcode())

print('This is a site connectivity checker')
while True:
    check = input('Check connectivity to a url?(Y/N):')
    if check.lower() == 'y':
        inp_url = input('Enter url to check:')
        conn_check(inp_url)
    elif check.lower() == 'n':
        quit()
    else:
        print('Invalid input')