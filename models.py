from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://img.favpng.com/17/6/12/rescue-dog-cat-animal-shelter-clip-art-png-favpng-Gt1HiZ98GPyWH2U8q7AquVtyC.jpg"

def connect_db(app):
    """Connect to DB"""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet"""
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default=True, nullable=False)
    
    
    def photo_url(self):
        return self.photo or DEFAULT_IMAGE_URL
