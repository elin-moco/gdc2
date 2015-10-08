import json
import sys
import time
import requests
import unicodecsv


if __name__ == '__main__':

    OUTFILE = 'toprepos.txt'
    repos = ''

    with open(sys.argv[1]) as f:
        reader = unicodecsv.DictReader(f)
        for row in reader:
            repos += '    \'' + row['repository_url'] + '\',\n'
    
    with open(OUTFILE, 'w') as f:
        f.write(repos[:-2])
