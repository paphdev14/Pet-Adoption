from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, Length, NumberRange, URL


class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[
                       InputRequired(message="Add Pet Name")])
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])

    photo = StringField("Photo URL", 
                        validators=[Optional(), URL()])
    age = IntegerField("Age", 
                       validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)])
    
    
class EditPetForm(FlaskForm):
    photo = StringField("Photo URL", 
                        validators=[Optional(), URL()])
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")