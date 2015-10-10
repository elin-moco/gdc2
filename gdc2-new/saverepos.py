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
          'created_at': repo.created_at.strftime("%Y-%m-%d %H:%M:%S"),
          'updated_at': repo.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
          'pushed_at': repo.pushed_at.strftime("%Y-%m-%d %H:%M:%S"),
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
    repos = {}

    with open(sys.argv[1]) as f:
        reader = unicodecsv.DictReader(f)
        for row in reader:
            repo_url = row['repo_url']
            if repo_url.startswith(REPO_API_URL):
                repo_name = repo_url[len(REPO_API_URL):]
                print repo_name
                repo = fetch_repo(repo_name)
                print repo
                time.sleep(2)
                if repo:
                    repos[repo_url] = repo
    
    with open(OUTFILE, 'w') as f:
        f.write(json.dumps(repos, indent=1))
