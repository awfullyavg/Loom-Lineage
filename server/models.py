from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)


    #relationships
    loom_id = db.Column(db.Integer, db.ForeignKey('looms.id'))
    families = db.relationship('Family', backref='user')

    #serialize rules
    serialize_rules = ('-families.user',)


class Family(db.Model, SerializerMixin):
    __tablename__= 'families'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    parent = db.Column(db.String) #Probably should be mother father
    partner = db.Column(db.String) #Might not need this. Parents should be enough? Parent = Partner?
    children = db.Column(db.String)
    sibling = db.Column(db.String)

    #relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    looms = db.relationship('Loom', backref='family')

    #serializers
    serialize_rules = ('-looms.family',)


class Loom(db.Model, SerializerMixin):
    __tablename__='looms'

    id = db.Column(db.Integer, primary_key=True)
    lineage = db.Column(db.String)
    photos = db.Column(db.String)

    #relationships
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    family_id = db.Column(db.Integer, db.ForeignKey('families.id'))
    users = db.relationship('User', backref='loom')

    #serializers
    serialize_rules = ('-event.looms', '-family.looms', '-user.looms')


class Event(db.Model, SerializerMixin):
    __tablename__='events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    #relationships
    looms = db.relationship('Loom', backref='event')

    #serializers
    serialize_rules = ('-looms.event',)

