from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "my-secret-app"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def root():
    """Homepage redirects to list of pets."""
    return redirect("/home")
# ==================================================


@app.route('/home')
def homepage():
    """Make Homepage Listing Pets"""
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add Pet"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        new_pet = Pet(name=name, species=species, photo=photo, age=age)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect('/home')
    else:
        return render_template('add_form.html', form=form)
        
@app.route('/home/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo = form.photo.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect('/home')
    else:
        return render_template('edit_form.html', form=form, pet=pet)
        