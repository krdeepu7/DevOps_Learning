import os
from flask import Flask, request, render_template
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test
collecion = db['flask-tutorial']

app = Flask(__name__)

@app.route('/')

def home():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')

    return render_template('index.html',day_of_week=day_of_week,current_time=current_time)

@app.route('/submit', methods = ["POST"])
def submit():
    form_data= dict(request.form)

    collecion.insert_one(form_data)
    return "success"


@app.route('/view')
def view():

    data = collecion.find()
    data = list(data)

    for item in data:
        print(item)
        del item['_id']
    
    data ={
        'data':data
    }

    return data


@app.route('/about')
def about():
    return "This is the about page of Module 6."

# @app.route('/api/<name>')
# # def name(name):
# #     print(f"Received request for name: {name}")
# #     length = len(name)
# #     if length > 5:
# #         return "Name is too long."
    
# #     else:
# #         return 'Nice name!'
    
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"{a} + {b} = {a + b}"

@app.route('/api')
def name():

    name = request.values.get('name')
    age = request.values.get('age')

    result = {'name':name,
            'age': age
    }

    return result

@app.route('/time')
def time():
    current_time = datetime.now().strftime('%H:%M:%S')
    return current_time



if __name__ == '__main__':

    app.run(debug=True)

