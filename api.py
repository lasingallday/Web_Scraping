#from werkzeug.exceptions import BadRequest
import os
import requests
from flask import Flask, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson import json_util

# insert your connection details here
# MONGO_URL = 'mongodb://<dbuser>:<pass>@<database URL>'
MONGO_URL = 'mongodb://localhost/27017'
# connect to the MongoDB server
client = MongoClient(MONGO_URL)
# connect to the default database within the server
db = client.get_default_database()

# db = client.test_database
# # get collection database
# profiles = db.test_profiles

import datetime
# post = {"author": "Jeff",
# 		"text": "My first blog post!",
# 		"tags": ["mongodb", "python", "pymongo"],
# 		"date": datetime.datetime.utcnow()}
# 
# post_id = posts.insert_one(post).inserted_id

# db.profiles.insert( { "_id":"jmclane","name":"John McLane",
# 					  "jobs":[{"employer":"NYPD","position":"Lieutenant","start":1988}]
#                     } )
db.profiles.insert( { "jobs":[{"employer":"NYPD","position":"Lieutenant","start":1988}]
                    } )
db.profiles.insert( { "jobs":[{"employer":"NYPD","position":"Officer","start":1990},
                             {"employer":"MIB","position":"Agent","start":1997}]
                    } )
db.profiles.insert( { "jobs":[{"employer":"Bag End","position":"Gardener","start":1954}]
                    } )

#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#page

app = Flask(__name__)
api = Api(app)

@app.route("/", methods=['GET'])
def hello():
	return "Hello world! Try /api/profiles or /api/companies for data."

# @app.route('/star/', methods=['GET'])
# def get_one_star(name):

# @app.route("/api/profiles", methods=['GET'])
# def list_profiles():
# 	fake_data = { "profiles": [ {"name":"John McLane","id":"jmclane"},
# 								{"name":"James Edwares","id":"jedwards"},
# 								{"name":"Samwise Gamgee","id":"sgamgee"} ]
# 				}
# 	return jsonify(fake_data)

# This works with inserted profiles, to test database
# listing all profiles
@app.route("/api/profiles", methods=['GET'])
def list_profiles():
    real_data = db.profiles.find()
    return( json_util.dumps({"profiles":real_data}) )

"""
db = {0: 'do the dishes',
	1: 'vacuum',
	2: 'mop',
	3: 'buy a new book'}

connect('')

#This is mongodb stuff
class User(Document):
	username = StringField()
	password = StringField()

class Todo(Document):
	task_id = IntField(unique=True)
	task = StringField(unique=True)
	
	def to_json(self):
		return {'task_id': self.task_id,
			'task': self.task}

class TodoListResource(Resource):
	def get(self, todo_id=None):
		try:
			todo = Todo.objects.get(task_id=todo_id)
			return todo.to_json()
		except DoesNotExist:
			raise BadRequest('todo with id %s does not exist' % todo_id)
	def put(self, todo_id):
		try:
			todo = Todo.objects.get(task_id=todo_id)
			todo.update(task=request.get_json()['message'])
		except DoesNotExist:
			raise BadRequest('todo with id %s does not exist' % todo_id)
	def post(self, todo_id):
		if todo_id not in db:
			db[todo_id] = request.get_json()['message']
		raise BadRequest('Resource does not exist')
	def delete(self, todo_id):
		if todo_id not in db:
			del db[todo_id]
			return{'success': 'True'}
		raise BadRequest('Resource does not exist')


api.add_resource(HelloWorld, '/', '/<int:todo_id>')
"""
db.dropDatabase()
if __name__ == '__main__':
	app.run(debug=True)

