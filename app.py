from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'Flask Store',
        'items': [
            {
                'name': 'Flask item',
                'price': 12.95
            }
        ]

    }
]
@app.route('/')
def home():
    return render_template('index.html')

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    # request made to endpoint "/store"
    # converts the string to a python dictionary
    # browser will send json data
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    # append the new store
    stores.append(new_store)
    # Return the new store as a jsonified string, otherwise, it will return a dictionary
    return jsonify(new_store)

# GET /store<string:name> fetches the name of the store
@app.route('/store/<string:name>')
def get_store(name):
    # iterate over stores
    for store in stores:
         # if store name matches, return it
        if store['name'] == name:
            return jsonify(store)
    # if no matches, return an error
    return jsonify({'message': 'Store could not be located.'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item: {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store could not be located.'})


# GET /store<string:name>/item
@app.route('/store/<string:name>/item')
def get_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({store['items']})
    return jsonify({'message', 'Store could not be located'})


if __name__ == "__main__":
    app.run(debug=True)
