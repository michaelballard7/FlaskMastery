from flask import Flask, request
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

        data = request.get_json(force=True) # recieve data from headers
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
