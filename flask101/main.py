from flask import Flask, jsonify, request

""" When building in flask think from the servers perspective"""

app = Flask(__name__)

stores = [
    {
        'name': 'Walmart',
        'items':[
            {
                'name':'dishsoap',
                'price': 2.99
            }
        ]
    }
]

@app.route("/")
def hello():
    return "Hello"

# Post - used to recieve data
# Get - used to send data back

# Post/store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    # allow my endpoint to capture json from the browser
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET/store/<string:name>
@app.route("/store/<string:name>", methods=["GET"]) # https://127.0.0.1:5000/store/some_name
def get_store(name):
    store = [store for store in stores if store['name'] == name]
    if store:
        return jsonify({"store": store})
    else:
        return jsonify({"error" : "store is not found"})

# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"stores":stores})  # json cannot be a list so I must make it into a dictionary

# POST /store/<string:name>/item {name:price}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({'store':store})
    return jsonify({'message':'store is not found'})


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message':"item is not found"})

app.run()
