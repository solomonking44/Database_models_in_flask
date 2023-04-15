from flask import Flask, render_template
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
api = Api(app)

#configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

#initialise the database
db = SQLAlchemy(app)

#create a model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    #create function to return string when we write something
    def __repr__(self):
        return '<Name %r>' % self.id

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/')
def about():
    return render_template('\about.html')

@app.route('/')
def gallery():
    return render_template('gallery.html')

class Student(Resource):
    def get(self, name):
        return f"Resource has been gotten {name}"

    def post(self, name):
        return f"{name} has been posted"

api.add_resource(Student, '/<name>')


