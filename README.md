Where does open source come from?
=================================

Sometimes a [picture](http://elin-moco.github.io/gdc2/) is worth a thousand
words.

This is an interactive visualization of the location of contributors to the
top repositories on GitHub.


Analyze Data
----------

The provided Makefile has everything needed to fetch data from
[GitHub Archive](http://githubarchive.org), load it into a database,
geocode locations and output the resulting JSON. It can even push
the results to GitHub pages.

There are also some interesting `queries` for doing things like fetching
top 200 repositories, gathering up all the relevant events or getting
the unique set of locations to geocode.

    # This first step takes hours and downloads ~6.5GB, change the Makefile for customizing data range
    make githubarchive

    # This step takes a few hours with decently fast disks
    make new-loaddb

    # Dump top 200 reops and generate sql queries for later use
    make new-toprepos

    # Dump user ids contributed in top 200 repos
    make new-topusers

    # Save repo data from github API
    make save-repos

    # Save user data from github API, this would take several hours due to API rate limit
    make save-users

    # This step geocodes any locations not already geocoded (`locations.json`)
    make new-geocode

    # Generate the `events.json` file used for the visualization
    make new-jsonify

For archive data before Dec 2014, the tasks to run in order would be githubarchive, loaddb, toprepos, geocode, jsonify.


Credits
-------

* Forked from [David Fischer](https://github.com/davidfischer/gdc2)'s earlier work.

* Geocoding by [Nominatim](http://wiki.openstreetmap.org/wiki/Nominatim),
  &copy; OpenStreetMap contributors.

* Inspired by earlier work by [Jens Finnäs](http://jensfinnas.com/dataist/ows/)
  and [Nanda Yadav](http://visual.ly/visualizing-nfl-draft-history)

* Built with [d3](http://d3js.org) by Mike Bostock
