"""Models for Cupcfrom"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete, update, ForeignKey

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


default_image= 'https://tinyurl.com/demo-cupcake'
class Cupcake(db.Model):
    __tablename = "cupcake"


    id = db.Column(db.Integer,primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=default_image) 
