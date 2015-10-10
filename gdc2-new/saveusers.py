import json
import sys
import time
import unicodecsv
from github import Github


gh = Github('elin-moco', '0315oshb5975')

def fetch_user(login):
    try:
        user =  gh.get_user(login)
        return {
          'login': user.login,
          'id': user.id,
          'avatar_url': user.avatar_url,
          'gravatar_id': user.gravatar_id,
          'type': user.type,
          'name': user.name,
          'company': user.company,
          'blog': user.blog,
          'location': user.location,
          'email': user.email,
          'hireable': user.hireable,
          'bio': user.bio,
          'public_repos': user.public_repos,
          'public_gists': user.public_gists,
          'followers': user.followers,
          'following': user.following,
          'created_at': user.created_at.strftime("%Y-%m-%d %H:%M:%S"),
          'updated_at': user.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        print e
        return None


if __name__ == '__main__':

    OUTFILE = 'users.json'
    users = {}

    with open(sys.argv[1]) as f:
        reader = unicodecsv.DictReader(f)
        for row in reader:
            print row['actor_login']
            user = fetch_user(row['actor_login'])
            print user
            time.sleep(1)
            if user:
                users[row['actor_login']] = user
    
    with open(OUTFILE, 'w') as f:
        f.write(json.dumps(users, indent=1))