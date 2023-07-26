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

api = Api(app) #may or may not use RESTful 

@app.route('/')
def home():
    return ''

class Users(Resource):
    def get(self):
        users_list = [user.to_dict(rules=('-families','-loom_id')) for user in User.query.all()]

        return make_response(users_list, 200)
api.add_resource(Users, '/users')


class UsersById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:
            return make_response('{error: "user not found"}', 404)
        
        return make_response(user.to_dict(rules=('-families','-loom_id')), 200) #Might want to get rid of the loom_id rule to see each users loom_id   
api.add_resource(UsersById, '/users/<int:id>')

class FamiliesById(Resource): #still needs a post, patch and delete
    def get(self, id):
        family = Family.query.filter(Family.id == id).first()

        if not family:
            return make_response('{error: "user not found"}', 404)
        
        return make_response(family.to_dict(), 200)
api.add_resource(FamiliesById, '/family/<int:id>') #Should it be '/user/family/<int:id>' ?


class Looms(Resource): #still needs a patch and delete
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

class Events(Resource): #still needs a patch and delete
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



if __name__ == '__main__':
    app.run(port=5555, debug=True)