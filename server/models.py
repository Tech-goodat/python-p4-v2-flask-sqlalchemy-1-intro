from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata=MetaData()

#creating a Flask SQLAlchemy extension
db=SQLAlchemy(metadata=metadata)

#define a model class by inheriting from db.model

class Pet(db.Model):
    __tablename__='pets'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    species=db.Column(db.String)