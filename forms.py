"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, URL, Optional

class AddPetForm(FlaskForm):
    "Form for adding pets."

    name = StringField(
        "Pet Name",
        validators=[InputRequired()],
    )

    species = SelectField(
        "Pet Species",
        choices=[
            ('cat','Cat'), ('dog','Dog'), ('porcupine','Porcupine')
        ],
        validators=[InputRequired()],
    )

    photo_url = StringField(
        "Pet Photo",
        validators=[Optional(), URL()],
    )

    age = SelectField(
        "Pet Age",
        choices=[
            ('baby','Baby'), ('young','Young'), ('adult','Adult'),
            ('senior','Senior')
        ],
        validators=[InputRequired()],
    )

    notes = StringField(
        "Pet Notes",
    )