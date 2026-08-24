from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection - "mongodb" is the service name from docker-compose.yml
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongodb:27017/")
client = MongoClient(MONGO_URI)
db = client["webapp_db"]
collection = db["messages"]

@app.route("/")
def home():
    messages = list(collection.find())
    return render_template("index.html", messages=messages)

@app.route("/add", methods=["POST"])
def add_message():
    name = request.form.get("name")
    message = request.form.get("message")
    if name and message:
        collection.insert_one({"name": name, "message": message})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)