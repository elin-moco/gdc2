import json
import sys
import time
import unicodecsv
from github import Github


REPO_API_URL = 'https://api.github.com/repos/'
gh = Github('elin-moco', '0315oshb5975')

def fetch_repo(repo_name):
    try:
        repo = gh.get_repo(repo_name)
        return {
          'id': repo.id,
          'name': repo.name,
          'full_name': repo.full_name,
          'description': repo.description,
          'created_at': repo.created_at.strftime("%Y-%m-%d %H:%M:%S") if repo.created_at else None,
          'updated_at': repo.updated_at.strftime("%Y-%m-%d %H:%M:%S") if repo.updated_at else None,
          'pushed_at': repo.pushed_at.strftime("%Y-%m-%d %H:%M:%S") if repo.pushed_at else None,
          'size': repo.size,
          'stargazers_count': repo.stargazers_count,
          'watchers': repo.watchers,
          'language': repo.language,
          'forks': repo.forks,
          'open_issues': repo.open_issues,
          'network_count': repo.network_count,
          'languages': repo.get_languages()
        }
    except Exception as e:
        print e
        return None


if __name__ == '__main__':

    OUTFILE = 'repos.json'
    try:
        with open(OUTFILE, 'r') as f:
            repos = json.loads(f.read())
        print "Found %s with %d repos" %(OUTFILE, len(repos.keys()))
    except Exception as e:
        print e
        repos = {}

    with open(sys.argv[1]) as f:
        reader = unicodecsv.DictReader(f)
        for row in reader:
            repo_url = row['repo_url']
            if repo_url.startswith(REPO_API_URL) and repo_url not in repos:
                repo_name = repo_url[len(REPO_API_URL):]
                print repo_name
                repo = fetch_repo(repo_name)
                print repo
                time.sleep(2)
                if repo:
                    repos[repo_url] = repo
    
    with open(OUTFILE, 'w') as f:
        f.write(json.dumps(repos, indent=1))
