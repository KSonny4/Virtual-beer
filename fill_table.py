import os

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from itertools import combinations

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "app.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class BeerPair(db.Model):
    beer_pair_id = db.Column(db.Integer, index = True, primary_key = True)
    #first name of participant
    name1 = db.Column(db.String(80))
    #second name of participant
    name2 = db.Column(db.String(80))
    #number of beers
    beers = db.Column(db.Integer)
    #0 if nobody, 1 if name1, 2 if name2
    side = db.Column(db.String(80))

    def __repr__(self):
        return "<Title: {} {} {} {}>".format(self.name1, self.name2, self.beers, self.side)


  
def fill():    
    users = ['Petr', 'Hofy', 'Krtek', 'Šimon', 'Víťa', 'Přěňěk', 'Sergej', 'Kuba','Ivan', 'Dita', 'Palec', 'Matouš']
    pairs = combinations(users,2)
    items = []
    for pair in pairs:
        items.append(dict(name1= pair[0], name2=pair[1], beers = '0', side=''))

    
    for item in items:        
        add_new = BeerPair(name1 = item['name1'], name2 = item['name2'], beers = item['beers'], side = item['side'])
        db.session.add(add_new)
    db.session.commit()
