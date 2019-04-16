from flask import Flask
from flask import jsonify
from flask import request

# create my mock json db
mock_db = [
    {
        "id":"07",
        "name":"Michael",
        "course": "Mathmatics"
     },
    {
        "id":"10",
        "name":"Tiffany",
        "course": "English"
     }
]

# instantiate my flask app
app = Flask(__name__)

# create my root route
@app.route("/", methods=["GET"])
def welcome():
    return "welcome to python web servivces by michael"

# create the test endpoint
@app.route("/test")
def testMe():
    return "Hello this is a reminder app"

# create a route to read all Students
@app.route("/student/getStudents",methods=["GET"])
def get_students():
    return jsonify({"students" : mock_db}) # do not forget to jsonify my responses

# create a route to read  a specific student
@app.route("/student/getStudent/<id>",methods=["GET"])
def get_student(id):
    student = [student for student in mock_db if(student['id'] == id)]
    return jsonify({"student" :student})

# to update a particular student
@app.route("/student/updateStudent/<id>",methods=["PUT"])
def update_student(id):
    student = [student for student in mock_db if(student['id'] == id)]
    if 'id' in request.json:
        print("student available")
    if 'id' in request.json:
        student[0]['name'] = request.json['name']
    return jsonify({"student" :student[0]})

# make a route to create a new student
@app.route("/student/addStudent",methods=["POST"])
def addStudent():
    student = {
        "id":request.json['id'],
        "name": request.json['name'],
        "course": request.json['course']
     }
    mock_db.append(student)
    return jsonify({"student" :mock_db})

# make a route to delete a specific student
@app.route("/student/removeStudent/<id>",methods=['DELETE'])
def removeStudent(id):
    student = [student for student in mock_db if(student['id'] == id)]
    print(student)
    if (len(student) > 0):
        mock_db.remove(student[0])
    return jsonify({"student": student})



if __name__ == '__main__':
    app.run()
