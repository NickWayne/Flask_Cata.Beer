from flask import session, redirect, url_for, render_template, request, jsonify
import requests
from .api import api_endpoints as api
from . import home

@home.route('/')
def index():
    beers = api.beers()
    # return jsonify(beers)
    return render_template("beers.html", username="testing", beers=beers)
    # return redirect(url_for('account.login'))

@home.route('/ingredients')
def ingredients():
    return api.ingredients()

@home.route('/stats')
def stats():
    return api.beers()

# @home.route('/landing')
# def landing():
#     """The landing page route, redirect users to their specific landing page.
#     """
#
#     if 'trainer' in session and 'type' in session:
#         return render_template("landing.html",account_type=session['type'], trainer=session['trainer'])
#
#     # return redirect(url_for('account.login'))
