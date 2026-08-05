from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API = "http://express-service:3000"

@app.route("/")
def home():
    students = requests.get(f"{API}/students").json()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add():

    data = {
        "name": request.form["name"],
        "course": request.form["course"]
    }

    requests.post(f"{API}/students", json=data)

    return redirect("/")

app.run(host="0.0.0.0", port=5000)