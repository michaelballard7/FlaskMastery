from flask import Flask
from flask_restful import Resource, Api

# define the app and api
app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self,name):
        item = [item for item in items if item['name'] == name]
        if item:
            return item
        else:
            return {'item':None}, 404

    def post(self, name):
        item = {'name':name,'price':12.00}
        items.append(item)
        return item, 201

api.add_resource(Item, '/item/<string:name>')

app.run()
