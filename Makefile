.PHONY: githubarchive tests loaddb jsonify geocode github


all: tests


# Must have required Python packages
new-loadgeo:
	@echo "Loading githubarchive data into local database."
	@echo "One month of data takes about one hour on my SSD."
	python gdc2-new/loadgeo.py


new-loaddb:
	@echo "Loading githubarchive data into local database."
	@echo "One month of data takes about one hour on my SSD."
	python gdc2-new/loaddb.py


loaddb:
	@echo "Loading githubarchive data into local database."
	@echo "One month of data takes about one hour on my SSD."
	python gdc2/loaddb.py


githubarchive:
	@echo "Downloading githubarchive.org data. This takes hours."
	mkdir -p githubarchive

	# Requires bash 4+ MacOS users may need to update or something
	cd githubarchive && wget 'http://data.githubarchive.org/2014-{10..12}-{01..31}-{0..23}.json.gz'


jsonify:
	sqlite3 github-events.db < queries/events.sql > events.csv
	python gdc2/jsonify.py events.csv
	@echo "www/data/events.json written"


geocode:
	sqlite3 github-events.db < queries/locations.sql > locations.csv
	python gdc2/geocoder.py locations.csv
	@echo "www/data/locations.json written"


toprepos:
	sqlite3 github-events.db < queries/toprepos.sql > toprepos.csv


github:
	ghp-import www
	git push origin gh-pages


tests:
	nosetests
