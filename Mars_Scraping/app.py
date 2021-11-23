from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping  

# set up Flask 
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set up App Routes
@app.route("/")
def index():
   # use PyMongo to find the "mars" collection in our database
   mars = mongo.db.mars.find_one()

   #  tell Flask to return an HTML template using an index.html file.
   return render_template("index2.html", mars=mars)

# Create scrape function
@app.route("/scrape")
def scrape():
   # assign a new variable that points to our Mongo database
   mars = mongo.db.mars

   # create a new variable to hold the newly scraped data using the scraping function we created
   mars_data = scraping.scrape_all()

   # Update the database
   mars.update({}, mars_data, upsert=True)

   # navigate our page back to / where we can see the updated content.
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()