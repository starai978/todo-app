from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.todo import Todo
from resources.test import Test

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

app.config['SECRET_KEY'] = 'disable the web security'
app.config['CORS_HEADERS'] = 'Content-Type'


api.add_resource(Todo, '/todos', '/todos/<string:id>')
api.add_resource(Test, '/', '/test', '/ping')