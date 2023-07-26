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

class UsersById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:
            return make_response('{error: "user not found"}', 404)
        
        return make_response(user.to_dict(), 200)
    
api.add_resource(UsersById, '/users/<int:id>')
        