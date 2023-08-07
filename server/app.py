from flask_restful import Resource
from flask import Flask, make_response, jsonify, request, session
from models import User, Family, Loom, Event
from config import db, app, api
import os



@app.route('/')
def home():
    return ''

class Users(Resource):
    def get(self):
        users_list = [user.to_dict(rules=('-families','-loom_id')) for user in User.query.all()]

        return make_response(users_list, 200)
    
    def post(self):
        data = request.get_json()

        try:
            new_user = User(
                fname = data['fname'],
                lname = data['lname'],
                email = data['email'],
                username = data['username'],
                _password_hash = data['_password_hash']
            )

            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(), 201)

        except ValueError:
            return make_response('{errors:["validation errors"]}', 400)
api.add_resource(Users, '/users')


class UsersById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:
            return make_response('{error: "user not found"}', 404)
        
        return make_response(user.to_dict(rules=('-families','-loom_id')), 200) #Might want to get rid of the loom_id rule to see each users loom_id   
api.add_resource(UsersById, '/users/<int:id>')

class Families(Resource):
    def get(self):
        family_list = [family.to_dict(rules=('-looms', '-user_id')) for family in Family.query.all()]
        return make_response(family_list, 200)
    
    def post(self):
        data = request.get_json()

        try:
            new_family = Family(
                name= data['name'],
                mother= data['mother'],
                father= data['father'],
                partner= data['partner'],
                children= data['children'],
            )

            db.session.add(new_family)
            db.session.commit()
            return make_response(new_family.to_dict(), 201)
        
        except ValueError:
            return make_response('{errors:["validation errors"]}', 400)
api.add_resource(Families, '/families')


class FamiliesById(Resource):
    def get(self, id):
        family = Family.query.filter(Family.id == id).first()

        if not family:
            return make_response('{error: "user not found"}', 404)
        
        return make_response(family.to_dict(), 200)
    
    def patch(self, id):
        family = Family.query.filter(Family.id == id).first()

        if not family:
            return make_response('Family not found', 404)
        try:
            data = request.get_json()
            for key in data:
                setattr(family, key, data[key])
            db.session.add(family)
            db.session.commit()
            return make_response(family.to_dict(), 202)
        except ValueError:
            return make_response('{errors:["validation errors"]}', 400)
        
    def delete(self, id):
        families = Family.query.filter(Family.id == id).first()

        if not families:
            return make_response('{errors:["validation errors"]}')
        
        db.session.delete(families)
        db.session.commit()
        return make_response('DELETED', 204)
api.add_resource(FamiliesById, '/family/<int:id>') #Should it be '/user/family/<int:id>' ?


class Looms(Resource):
    def get(self):
        looms_list = [loom.to_dict() for loom in Loom.query.all()]

        return make_response(looms_list, 200)
    
    def post(self):
        data = request.get_json()

        try:
            new_loom = Loom(
                lineage = data['lineage'],
                photos = data['photos'], #Might want to take this out and have users add via frontend.
                family_id = data['family_id'],
                event_id = data['event_id']
            )

            db.session.add(new_loom)
            db.session.commit()
            return make_response(new_loom.to_dict(), 201)

        except ValueError:
            return make_response('{errors:["validation errors"]}', 400)
api.add_resource(Looms, '/looms')

class LoomsById(Resource):
    def patch(self, id):
        loom = Looms.query.filter(Loom.id == id).first()

        if not loom:
            return make_response('Loom not found', 404)
        try:
            data = request.get_json()
            for key in data:
                setattr(loom, key, data[key])
            db.session.add(loom)
            db.session.commit()
            return make_response(loom.to_dict(), 202)
        except ValueError:
            return make_response('{errors:["validation errors"]}', 400)

    def delete(self, id):
        looms = Loom.query.filter(Loom.id == id).first()

        if not looms:
            return make_response('{errors:["validation errors"]}')
        
        db.session.delete(looms)
        db.session.commit()
        return make_response('DELETED', 204)
api.add_resource(LoomsById, '/looms/<int:id>')

class Events(Resource):
    def get(self):
        events_list = [event.to_dict() for event in Event.query.all()]

        return make_response(events_list, 200)
    
    def post(self):
        data = request.get_json()

        try:
            new_event = Event(
                name = data['name'],
                description = data['description']
            )

            db.session.add(new_event)
            db.session.commit()
        
        except ValueError:
            return make_response('{errors:["validation errors"]}', 400)
api.add_resource(Events, '/events')

class EventsById(Resource):
    def get(self, id):
        events = Event.query.filter(Event.id == id).first()

        if not events:
            return make_response('{error: "event not found"}', 404)
        
        return make_response(events.to_dict(), 200)
    
    def patch(self, id):
        event = Event.query.filter(Event.id == id).first()

        if not event:
            return make_response('Event not found', 404)
        try:
            data = request.get_json()
            for key in data:
                setattr(event, key, data[key])
            db.session.add(event)
            db.session.commit()
            return make_response(event.to_dict(), 202)
        except ValueError:
            return make_response('{errors:["validation errors"]}', 400)
        
    def delete(self, id):
        events = Event.query.filter(Event.id == id).first()
        if not events:
            return make_response({"error: Event not found"}, 404)
        
        db.session.delete(events)
        db.session.commit()
        return make_response('DELETED', 204)
api.add_resource(EventsById, '/events/<int:id>')

class Login(Resource):

    def get(self):
        pass

    def post(self):
        data = request.get_json()
        username = data['username']
        user = User.query.filter(User.username == username).first()
        #Grab password
        # password = data['password']
        # # print(user)
        # #Test to see if password matches
        # if user:
        #     if user.authenticate(password):
        #         session['user_id'] = user.id
        # return make_response({'error': 'Invalid username or password'}, 401)
        if user:
            session['user_id'] = user.id

            response = make_response(
                jsonify(user.to_dict()), 201)
        else:
            response = make_response({}, 404)
        
        return response
api.add_resource(Login, '/login')

class Logout(Resource):
    def delete():
        session['user_id'] = None

        response = make_response({}, 204)

        return response
api.add_resource(Logout, '/logout')

class Check_Session(Resource):
    def get(self):
        user_id = session.get('user_id')

        if user_id:
            user = User.query.filter(User.id == user_id).first()

            response = make_response(user.to_dict(), 200)
        else:
            response = make_response({}, 400)
        return response
api.add_resource(Check_Session, '/check_session')

if __name__ == '__main__':
    app.run(port=5555, debug=True)