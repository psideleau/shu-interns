# This is the file that implements a flask server to do inferences. It's the file that you will modify to
# implement the scoring for your own algorithm.

from __future__ import print_function
from collections import namedtuple
import os
import json
import flask
from flask import jsonify
import constants 
from flask import render_template
from datetime import datetime
from student  import StudentSummary 

# The flask app for serving predictions
app = flask.Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    """Determine if the container is working and healthy. In this sample container, we declare
    it healthy if we can load the model successfully."""
    #health = ScoringService.get_model() is not None  # You can insert a health check here
    # status = 200 if health else 404
    status = 200 
    return flask.Response(response='\n', status=status, mimetype='application/json')


def _response_if_error_else_request_body():
    if  (not ('X-Auth-Token' in flask.request.headers and flask.request.headers['X-Auth-Token'] == constants.AUTHENTICATION_TOKEN)):
        return flask.Response(status=401), None

    if (not flask.request.is_json):
         return flask.Response(response='json is required', status=400, mimetype='text/html'), None
    
    body = flask.request.json
    if (not('language' in body and 'answer' in body)):
        return flask.Response(response='langauge and answer properties are required', status=400, mimetype='text/html'), None
    
    if ('en' != body['language'].lower()):
        return flask.Response(response='Only English is supported', status=501, mimetype='text/html'), None

    return None, body


@app.route('/students', methods=['GET'])
def find_students():
    student1 = StudentSummary(id=8000000, first_name="paul", last_name="sideleau", graduation_year=2001)
    student2 = StudentSummary(id=8000000, first_name="paul", last_name="sideleau", graduation_year=2001)
    return jsonify([student2._asdict(), student1._asdict()])

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )