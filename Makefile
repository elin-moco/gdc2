.PHONY: githubarchive tests loaddb toprepos geocode jsonify github


all: tests


githubarchive:
	@echo "Downloading githubarchive.org data. This takes hours."
	mkdir -p githubarchive

	# Requires bash 4+ MacOS users may need to update or something
	cd githubarchive && wget 'http://data.githubarchive.org/2015-{10..12}-{01..31}-{0..23}.json.gz'


### tasks for new githubarchive format (start from Jan 2015) ###

new-loaddb:
	@echo "Loading githubarchive data into local database."
	@echo "One month of data takes about one hour on my SSD."
	python gdc2-new/loaddb.py


new-toprepos:
	sqlite3 github-events-new.db < queries/toprepos-new.sql > toprepos-new.csv
	python gdc2-new/toprepos.py toprepos-new.csv
	cat queries/users.sql.head toprepos-new.txt queries/users.sql.tail > queries/users.sql
	cat queries/events-new.sql.head toprepos-new.txt queries/events-new.sql.tail > queries/events-new.sql
	@echo "queries/users.sql, queries/events-new.sql written"


new-topusers:
	sqlite3 github-events-new.db < queries/users.sql > users.csv
	@echo "users.csv written"


save-repos:
	python gdc2-new/saverepos.py toprepos-new.csv
	@echo "repos.json written"


save-users:
	python gdc2-new/saveusers.py users.csv
	@echo "users.json written"


new-geocode:
	python gdc2-new/userlocs.py
	python gdc2/geocoder.py locations.csv


new-jsonify:
	sqlite3 github-events-new.db < queries/events-new.sql > events-new.csv
	python gdc2-new/jsonify.py events-new.csv
	@echo "www/data/events-new.json written"

### end oftasks for new githubarchive format (start from Jan 2015 ) ###

### tasks for old githubarchive format (before Dec 2014) ###

loaddb:
	@echo "Loading githubarchive data into local database."
	@echo "One month of data takes about one hour on my SSD."
	python gdc2/loaddb.py


toprepos:
	sqlite3 github-events.db < queries/toprepos.sql > toprepos.csv
	python gdc2/toprepos.py toprepos.csv
	cat queries/events.sql.head toprepos.txt queries/events.sql.tail > queries/events.sql
	cat queries/locations.sql.head toprepos.txt queries/locations.sql.tail > queries/locations.sql
	@echo "queries/events.sql,queries/locations.sql written"


geocode:
	sqlite3 github-events.db < queries/locations.sql > locations.csv
	python gdc2/geocoder.py locations.csv
	@echo "www/data/locations.json written"


jsonify:
	sqlite3 github-events.db < queries/events.sql > events.csv
	python gdc2/jsonify.py events.csv
	@echo "www/data/events.json written"

### end of tasks for old githubarchive format (before Dec 2014) ###


github:
	ghp-import www
	git push origin gh-pages


tests:
	nosetests
