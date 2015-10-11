import json

def cleanup_location(location):
    if location:
        return ' '.join(location.replace(',', ' ').replace('.', ' ').split())
    return None

try:
    locs = set()
    with open('users.json', 'r') as f:
        USERS = json.loads(f.read())
        for login, user in USERS.iteritems():
            locs.add(cleanup_location(user['location']))

    userlocs = 'location\n'
    for loc in locs:
        if loc:
            userlocs += '"' + loc + '"\n'
    with open('locations.csv', 'w') as f:
        f.write(userlocs.encode("utf-8"))

except IOError:
    sys.stderr.write('users.json should be there\n')
    sys.exit(1)
