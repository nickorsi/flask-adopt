"""Flask app for adopt app."""

import os

from flask import Flask, flash, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

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

    pets = Pet.query.order_by('name').all()

    return render_template(
        'home.html',
        pets=pets
    )

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''Show add pet form and handle add pet'''

    form = AddPetForm()

    if form.validate_on_submit():

        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data,
        )

        db.session.add(pet)
        db.session.commit()

        flash('Pet added!')
        return redirect('/')

    else:

        return render_template(
            'add-pet-form.html',
            form=form,
        )

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Show edit pet form and handle edit pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash('Pet edited!')
        return redirect('/')

    else:
        return render_template(
            "display-edit-pet-form.html",
            pet=pet,
            form=form,
        )
