from flask import Flask
from flask_restful import Resource, Api
# 'Resource' allows to create a resource to connect to , 'Api' a wrapper around the application that allows that resource to connect

app = Flask(__name__)

api = Api(app)

#creating a resource
class HelloWorld(Resource):
    def get(self):
        return {"hello":"world"}  #this dictionary is going to be read as JSON

#connecting the resource to a URL
api.add_resource(HelloWorld, '/') # '/' is the url for this case


if __name__ == "__main__":
    app.run(debug= True)