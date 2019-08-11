from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

puppies = []

class PuppyNames(Resource):
    def get(self, name): # very important all the methods (get, post, delete) must have the same parameters
        for pup in puppies:
            if pup['name'] == name:
                return pup
        return {'name':None},404 
        # we are returning a tuple where the first value is a dict showing that the value asked doesnt exist
        # and the second one is an http status: 404 which means not found,
        # we could have returned just the dict without the ', 404' but then the status would have been '200 OK'
        # we want it to be 404 in the scenario where the name doesnt exist

    def post(self, name):
        pup = {'name':name}
        puppies.append(pup)
        return pup

    def delete(self, name):
        for index, pup in enumerate(puppies):
            if pup['name'] == name:
                deleted_pup = puppies.pop(index) #the important part here is puppies.pop(ind)
                return {'note':'delete succes'}


class AllNames(Resource):
    def get(self):
        return {'puppies': puppies}

api.add_resource(PuppyNames, '/puppy/<string:name>') 
api.add_resource(AllNames, '/puppies') 

if __name__ == "__main__":
    app.run(debug= True)