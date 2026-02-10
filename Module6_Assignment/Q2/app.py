from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.server_api import ServerApi
import os

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client.test
collecion = db['flask-tutorial']

@app.route("/")
def form():
    return render_template("form.html", error=None)


@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "age": int(request.form.get("age")),
        }

        collecion.insert_one(data)

        return redirect(url_for("success"))

    except Exception as e:
        return render_template("form.html", error=str(e))


@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == '__main__':

    app.run(debug=True)