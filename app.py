from flask import Flask
from api.users import users_bp
from api.items import items_bp

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return {"message": "Flask API CI/CD Working", "status": "success"}

app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(items_bp, url_prefix="/api/items")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
