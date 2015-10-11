import json
import sys
import time
import requests
import unicodecsv


GITHUB_URL = 'https://github.com/'

if __name__ == '__main__':

    OUTFILE = 'toprepos.txt'
    OUTFILE2 = 'www/data-repos.js'
    repos = ''
    repo_names = '[\n  "",\n'

    with open(sys.argv[1]) as f:
        reader = unicodecsv.DictReader(f)
        for row in reader:
            repo_url = row['repository_url']
            repos += '    \'' + repo_url + '\',\n'
            if repo_url.startswith(GITHUB_URL):
            	repo_names += '  "' + repo_url[len(GITHUB_URL):] + '",\n'
    
    with open(OUTFILE, 'w') as f:
        f.write(repos[:-2])

    with open(OUTFILE2, 'w') as f:
        f.write(repo_names[:-2] + '\n]')
