import os

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "virtualbeer.db"))

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
        return "<Title: {} {} {} {}>".format(self.name1, self.name2, self.beers, self.side)






@app.route("/update_first/<beer_pair_id>", methods=["POST"])
def update_first(beer_pair_id):
    try:
        print('name: {}, id: {}'.format('1', beer_pair_id))        
        current_beer_count = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update beerPair")
        print(e)
    return redirect("/")

@app.route("/update_second/<beer_pair_id>", methods=["POST"])
def update_second(beer_pair_id):
    try:
        print('name: {}, id: {}'.format('2', beer_pair_id))
    except Exception as e:
        print("Couldn't update beerPair")
        print(e)
    return redirect("/")

@app.route("/", methods=["GET"])
def home():    
    beerpairs = BeerPair.query.all()
    return render_template("home.html", beerpairs=beerpairs)

  
if __name__ == "__main__":
    app.run(debug=True)


