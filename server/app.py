from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, make_response, jsonify, request
from models import db, User, Family, Loom, Event
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

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
                password = data['password']
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
        family_list = [family.to_dict() for family in Family.query.all()]
        return make_response(family_list, 200)
    
    def post(self):
        data = request.get_json()

        try:
            new_family = Family(
                name= data['name'],
                mother= data['mother'],
                father= data['father'],
                partner= data['partner'],
                children= ['children'],
                # sibling= data['sibling'] If I have two children that auto amkes them siblings. 
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
                photos = data['photos'],
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

if __name__ == '__main__':
    app.run(port=5555, debug=True)