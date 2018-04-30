from flask import current_app

# Sets up the db service library to interface with the website api
from .brewerydb import *
BreweryDb.configure("c6a44f4ad5bb5961c187c4b6e968953c")


def search(query, type):
    """Searches the db, based on the query string and the type
        query: string
        type: "beer" or "brewery"
        return: json object list or []
    """
    try:
        if type == "beer":
            return BreweryDb.search({'q': query, 'type': type, 'withBreweries': 'Y'})['data']
        else:
            return BreweryDb.search({'q': query, 'type': type})['data']
    except Exception:
        return []

def beer(id):
    """Finds the beer by id in the db and returns it with brewery info
        id: string
        return: json object list or []
    """
    try:
        return BreweryDb.beer(id, {'withBreweries': 'Y'})['data']
    except Exception:
        return []

def ingredients(id):
    """Finds the beers ingredients from the db, or returns an empty json list
        id: string
        return: json object list or empty json list
    """
    if id == "":
        return "None"
    else:
        try:
            return BreweryDb.beer(id + "/ingredients")['data']
        except Exception:
            return [{"category": "", "name": ""}]

def breweries(id):
    """Finds the brweery associated with the id provided
        id: string
        return: json object list or []
    """
    try:
        return BreweryDb.brewery(id)['data']
    except Exception:
        return []

def breweryBeers(id):
    """Finds the beers that belong to the brewery with the id provided
        id: string
        return: json object list or empty json list
    """
    try:
        # [:-1:] this is because the id has a - added to the end to indicate
        # that it is for this method, removes the last character from a string
        return BreweryDb.brewery(id[:-1:] + "/beers")['data']
    except Exception:
        return id[:-1:] + "/beers"
