from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from config import db, bcrypt



class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)

    @validates('username')
    def validates_username(self, key, username):
        if username and len(username) > 0:
            return username
        else:
            raise ValueError('Username is to short')



    #relationships
    loom_id = db.Column(db.Integer, db.ForeignKey('looms.id'))
    families = db.relationship('Family', backref='user')

    #serialize rules
    serialize_rules = ('-families.user',)


class Family(db.Model, SerializerMixin):
    __tablename__= 'families'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    mother = db.Column(db.String) #Was parent
    father = db.Column(db.String)
    partner = db.Column(db.String)
    children = db.Column(db.String)

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

