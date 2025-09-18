import json
from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)  # Create instance of Flask
api = Api(app)  # Initialize Flask-RESTful extension

class Student(Resource):  # Create resource as class
    def get(self, id):  # Define method to handle HTTP GET requests
        match id:
            case 1:
                name = "Jane Student"
            case 2:
                name = "Abdul Student"
            case _: 
                name = "Jose Smith"
        
        return jsonify({'name': name})  # Return data (will be converted to JSON response with status code 200)

    def post(self):
        pass

# Configure route within API
# GET requests to URL /api/student will call Student.get
api.add_resource(Student,'/api/participants/<int:id>', endpoint="student")  

if __name__ == '__main__':
    app.run(debug=True)  # Launch development server with Flask app

