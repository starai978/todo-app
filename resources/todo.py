from flask_restful import Resource, reqparse
from uuid import uuid1
import time

todos = [{
    'id': str(uuid1()),
    'title': 'visit volkswagen showroom',
    'isCompleted': True
}, {
    'id': str(uuid1()),
    'title': 'visit skoda showroom',
    'isCompleted': True
}, {
    'id': str(uuid1()),
    'title': 'check with toyota',
    'isCompleted': False
}, {
    'id': str(uuid1()),
    'title': 'get a test drive from all visited cars',
    'isCompleted': False
}]

parser = reqparse.RequestParser()
parser.add_argument('title')


class Todo(Resource):
    def get(self):
        time.sleep(3)
        return todos

    def post(self):
        data = parser.parse_args()
        todo = {
            'id': str(uuid1()),
            'title': data.get('title'),
            'isCompleted': False
        }
        todos.append(todo)

        return todo, 201
