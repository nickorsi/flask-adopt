"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, Optional

class AddPet(FlaskForm):
    "Form for adding pets."

    name = StringField(
        "Pet Name",
        validators=[InputRequired()],
    )

    species = StringField(
        "Pet Species",
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
        validators=[],
    )

    notes = SelectField(
        "Pet Notes",
    )