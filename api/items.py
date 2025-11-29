from flask import Blueprint, request, jsonify

items_bp = Blueprint("items", __name__)

items = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 25000}
]

@items_bp.get("/")
def get_items():
    return jsonify(items)

@items_bp.post("/")
def add_item():
    data = request.json
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    new_id = items[-1]["id"] + 1 if items else 1
    item = {"id": new_id, "name": data["name"], "price": data["price"]}
    items.append(item)
    return jsonify(item), 201
