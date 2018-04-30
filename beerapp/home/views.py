import requests
from flask import session, redirect, url_for, render_template, request, jsonify
from operator import itemgetter
from .api import api_endpoints as api
from . import home

# These set up routes for index and index with an id after it for the beer ids
@home.route('/<id>', methods=["GET", "POST"])
@home.route('/', methods=["GET", "POST"])
def index(error="", id="", ingredients = ""):
    if request.method == "GET": # All GET requests for index route
        if id != "" and id[-1] == "-": # The - is added to the id string to indicate the ids for brewery beers
                beers = api.breweryBeers(id)
        else:
            beers = []
            beers.append(api.beer(id))# need to add to list because of the iteration of the html file
            ingredients = api.ingredients(id)
            if ingredients == "None":
                error = "Search For Beers" # Makes the page display this message under search bar

        # Renders the beers page with the beers, ingredients, and errors passed in. logic in beers.html
        return render_template("beers.html", beers=beers, ingredients=ingredients, error=error)

    elif request.method == "POST": # All POST requests for index route
        # Searches the breweryapi for the name of the beer
        # NOTE: the searching inside the api is atrocious, I can't improve it without
        # Destroying thje preformance of the site dramatically
        beers = api.search(request.form.get('name'), "beer")

        # If there is no beers returned in the search, return the error no beers
        if beers == []:
            error = "No beers Match"

        # Renders the beers page with the beers, and errors passed in. logic in beers.html
        return render_template("beers.html", beers=beers, error=error)

# These set up routes for /breweries and /breweries with an id after it for the breweries id
@home.route('/breweries/<id>', methods=["GET", "POST"])
@home.route('/breweries/', methods=["GET", "POST"])
def breweries(name="", id="", error=""):
    if request.method == "GET": # All GET requests for index route
        if id != "": # Add the info for the brewery of that id to the breweries list
            breweries = []
            breweries.append(api.breweries(id))

        # If there have been no searches, return search for breweries error
        else:
            breweries = []
            error = "Search For Breweries"

        # Renders the beers page with the breweries, and errors passed in. logic in breweries.html
        return render_template("breweries.html", breweries=breweries, error=error)


    elif request.method == "POST": # All POST requests for index route
        # Searches the breweryapi for the name of the brewery
        # NOTE: the searching inside the api is atrocious, I can't improve it without
        # Destroying thje preformance of the site dramatically
        breweries = api.search(request.form.get('name'), "brewery")

        # If there is no breweries returned in the search, return the error no breweries
        if breweries == []:
            error = "No Breweries Match"

        # Renders the beers page with the breweries, and errors passed in. logic in breweries.html
        return render_template("breweries.html", breweries=breweries, error=error)
