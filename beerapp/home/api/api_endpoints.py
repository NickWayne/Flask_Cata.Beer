from flask import current_app
from collections import defaultdict
from .brewerydb import *
BreweryDb.configure("c6a44f4ad5bb5961c187c4b6e968953c")

def beers():
    return BreweryDb.beers({'styleId': "48", "hasLabels": "Y", 'withBreweries': 'Y'})['data']

def search(query, type):
    try:
        if type == "beer":
            return BreweryDb.search({'q': query, 'type': type, 'withBreweries': 'Y'})['data']
        else:
            return BreweryDb.search({'q': query, 'type': type})['data']
    except Exception:
        return []

def breweries(name):
    try:
        return BreweryDb.brewery(name)['data']
    except Exception:
        return []

def getStyles():
    styles = BreweryDb.styles()['data']
    groupids = defaultdict(list)
    styleGroups = []
    for style in styles:
        groupids[style['category']['name']].append(style['id'])
        styleGroups.append(style['category']['name'])
    return [list(set(styleGroups)),groupids, styles]



def ingredients():
    return BreweryDb.beer('WHQisc')
