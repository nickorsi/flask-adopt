"""Flask app for adopt app."""

import os

from flask import Flask, flash, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False #---> Switch for redirect pause page, False=off True=on
app.debug = True #---> Switch for debug toolbar, False=off True=on
debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #---> When using SQL Alchemy
app.config['SQLALCHEMY_ECHO'] = True #---> When using SQL Alchemy

connect_db(app)


@app.get('/')
def index():
    '''Homepage to list pets'''

    pets = Pet.query.all()

    return render_template(
        'home.html',
        pets=pets
    )