from flask import Blueprint, request, jsonify

users_bp = Blueprint("users", __name__)

users = {
    1: {"id": 1, "name": "Javed", "role": "admin"},
    2: {"id": 2, "name": "John Doe", "role": "user"}
}

@users_bp.get("/")
def get_users():
    return jsonify(list(users.values()))

@users_bp.get("/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@users_bp.post("/")
def create_user():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    new_id = max(users.keys()) + 1
    users[new_id] = {"id": new_id, "name": data["name"], "role": data.get("role", "user")}
    return jsonify(users[new_id]), 201

@users_bp.delete("/<int:user_id>")
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    deleted = users.pop(user_id)
    return jsonify({"deleted": deleted})
