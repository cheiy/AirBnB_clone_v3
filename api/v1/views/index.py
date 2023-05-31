#!/usr/bin/python3
"""
App views for AirBnB_clone_v3
"""

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def status():
    """ return status """
    status = {"status": "OK"}
    return jsonify(status)
