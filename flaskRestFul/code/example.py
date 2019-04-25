
from flask import Flask
from flask_restful import Resource, Api

# define the app and api
app = Flask(__name__)
api = Api(app)

# define the resource
class Student(Resource):
    # define the methods the resource can use
    def get(self, name):
        return {'student': name }

# add the resource to the api and add the route to be called
api.add_resource(Student, '/student/<string:name>') # creates http://127.0.0.1:5000/student/some_name


app.run(port=5000)
