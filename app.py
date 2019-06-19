import os

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

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
    side = db.Column(db.Integer)

    def __repr__(self):
        return "<name1: {} name2: {} beers: {} side: {}>".format(self.name1, self.name2, self.beers, self.side)



def update_beer_count(beerpair, name):
	if beerpair.side == '':
		beerpair.side = '{} {}'.format(name, 'owns beer(s)')
		beerpair.beers += 1
	elif name in beerpair.side:
		beerpair.beers += 1
	else:
		beerpair.beers -= 1

	if beerpair.beers == 0:
		beerpair.side = ''
	db.session.commit()
	beerpairs = BeerPair.query.all()
	return render_template("home.html", beerpairs=beerpairs)



@app.route("/update_first/<beer_pair_id>", methods=["POST"])
def update_first(beer_pair_id):
    try:        
        beerpair = BeerPair.query.get(beer_pair_id)
        print(beerpair)
        update_beer_count(beerpair, beerpair.name1)                
    except Exception as e:
        print("Couldn't update beerPair")
        print(e)
    return redirect("/")

@app.route("/update_second/<beer_pair_id>", methods=["POST"])
def update_second(beer_pair_id):
    try:        
        beerpair = BeerPair.query.get(beer_pair_id)
        print(beerpair)
        update_beer_count(beerpair, beerpair.name2)        
    except Exception as e:
        print("Couldn't update beerPair")
        print(e)
    return redirect("/")

@app.route("/", methods=["GET"])
def home():    
    beerpairs = BeerPair.query.all()
    return render_template("home.html", beerpairs=beerpairs)

  
#logic of code works only if names are unique
if __name__ == "__main__":
    app.run(debug=True)


