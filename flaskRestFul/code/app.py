from flask import Flask, request
from flask_restful import Resource, Api
from secrets import *

# define the app and api
app = Flask(__name__)
app.secret_key = SECRET_KEY
api = Api(app)

items = []

class Item(Resource):
    def get(self,name):
        item = next(filter(lambda x: x['name'] == name, items),None) # next returns the first item returned by a filter function
        return {'item':item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items),None):
            return {f"message": "An item with the name {name} exists already"},400

        data = request.get_json() # recieve data from headers
        item = {'name':data['name'],'price':data['price']}
        items.append(item)
        return item, 201

    # def delete(self,name):
    #     item = [item for item in items if item['name'] == name]
    #     if item:
    #         del items[name]
    #         return items
    #     else:
    #         return {"error, object not for or deleted"}, 404

class ItemList(Resource):
    def get(self):
        if items:
            return {"items":items}, 201
        else:
            return {"items": None}, 404


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
