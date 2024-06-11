#!/usr/bin/python3

"""
Create Flask app
"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET', ])
def api_status():
    """
    Returns the status of the API
    """
    response = {'status': 'OK'}
    return jsonify(response)