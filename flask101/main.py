from flask import Flask

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
    pass

# GET/store/<string:name>
@app.route("/store/<string:name>", methods=["GET"]) # https://127.0.0.1:5000/store/some_name
def get_store(name):
    pass

# GET /store
@app.route("/store")
def get_stores():
    pass


# POST /store/<string:name>/item {name:price}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    pass
