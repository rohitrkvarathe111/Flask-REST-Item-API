from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample initial data
items = [
    {"id": 1, "name": "Item 1", "add": 456},
    {"id": 2, "name": "Item 2", "add": 789},
    {"id": 3, "name": "Item 3", "add": 123},
    {"id": 4, "name": "Item 4", "add": 963},
    {"id": 5, "name": "Item 5", "add": 852},
    {"id": 6, "name": "Item 6", "add": 741}
    
]
next_id = 7 


@app.route("/")
def hello():
    return ("hello , welcome to my website")

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    global next_id
    data = request.json
    new_item = {"id": next_id, "name": data["name"], "add":data["add"]}
    items.append(new_item)
    next_id += 1
    return jsonify(new_item), 201

# Get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return "Item not found", 404
    return jsonify(item)

# Update an item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return "Item not found", 404
    item["name"] = data["name"]
    return jsonify(item)

# Delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return "Item deleted", 204

if __name__ == '__main__':
    app.run(debug=True)
