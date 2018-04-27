from flask import session, redirect, url_for, render_template, request, jsonify
from operator import itemgetter
import requests
from .api import api_endpoints as api
from . import home

@home.route('/<id>', methods=["GET", "POST"])
@home.route('/', methods=["GET", "POST"])
def index(error="", id=""):
    ingredients = ""
    if request.method == "GET":
        if id != "" and id[-1] == "-":
                beers = api.breweryBeers(id)
        else:
            beers = []
            beers.append(api.beer(id))
            ingredients = api.ingredients(id)
            if ingredients == "None":
                error = "Search For Breweries"
        return render_template("beers.html", beers=beers, ingredients=ingredients, error=error)
    elif request.method == "POST":
        beers = api.search(request.form.get('name'), "beer")
        if beers == []:
            error = "No beers Match"
        return render_template("beers.html", beers=beers, error=error)

@home.route('/breweries/<id>', methods=["GET", "POST"])
@home.route('/breweries/', methods=["GET", "POST"])
def breweries(name="", id="", error=""):
    if request.method == "GET":
        if id != "":
            breweries = []
            breweries.append(api.breweries(id))
        else:
            breweries = []
            error = "Search For Breweries"
        # return jsonify(breweries)
        return render_template("breweries.html", breweries=breweries, error=error)
    elif request.method == "POST":
        breweries = api.search(request.form.get('name'), "brewery")
        # return jsonify(breweries)
        if breweries == []:
            error = "No Breweries Match"
        return render_template("breweries.html", breweries=breweries, error=error)
