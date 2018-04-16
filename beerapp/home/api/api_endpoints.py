from flask import current_app
from .brewerydb import *
BreweryDb.configure("c6a44f4ad5bb5961c187c4b6e968953c")

def beers():
    return BreweryDb.beers({'p': 1, 'availableId': 1, 'hasLabels': 'Y'})['data']

def ingredients():
    return BreweryDb.beer('WHQisc')
