import os
from app import app
from flask import render_template, request, redirect




from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'events'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://dbUser:aY9m2EzN9qAH2nf3@cluster0-1mug4.mongodb.net/events?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    #connect to the database
    collection = mongo.db.events
    #query the database
    #store those events as a list of dictionaries called events
    events = list(collection.find({}))
    #print the events
    for event in events:
        print(event["event_name"])
        print(event["event_date"])
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    collection = mongo.db.events

    # insert new data
    collection.insert({"event_name": "test", "event_date": "today"})

    # return a message to the user
    return "you added an event to the database."

@app.route('/results', methods = ["get", "post"])

def results():
    # store userinfo from the form
    user_info = dict(request.form)
    print(user_info)
    # get the event_name and the event_date and store them
    event_name = user_info["event_name"]
    print("the event name is", event_name)

    event_date = user_info["event_date"]
    print("the event date is", event_date)

    event_type = user_info["category"]
    print(event_type)

    # connect to the database
    collection = mongo.db.events

    # insert new data
    collection.insert({"event_name": event_name, "event_date": event_date, "event_type": event_type})

    # return a message to the user
    return redirect("/index")

@app.route("/secret")
def secret():
    #connect to the database
    collection = mongo.db.events
    #delete everything from the database
    #invoke the delete_many method on the collection
    collection.delete_many({})
    return redirect('/index')


@app.route("/social")
def social():
    collection = mongo.db.events
    social = list(collection.find({"event_type": "social"}))
    print (social)
    return render_template('index.html', events = social)

@app.route("/work")
def work():
    collection = mongo.db.events
    work = list(collection.find({"event_type": "work"}))
    print (work)
    return render_template('index.html', events = work)

@app.route("/school")
def school():
    collection = mongo.db.events
    school = list(collection.find({"event_type": "school"}))
    print (school)
    return render_template('index.html', events = school)

@app.route("/afterschool")
def afterschool():
    collection = mongo.db.events
    afterschool = list(collection.find({"event_type": "afterschool"}))
    print (afterschool)
    return render_template('index.html', events = afterschool)
