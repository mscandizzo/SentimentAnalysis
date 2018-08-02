from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/tweets"
mongo = PyMongo(app)

@app.route("/")
def demo_list():
    gld_tweets = mongo.db.tweets.find({},{'text':1,"_id":0}).limit(5)
    return render_template("testj2.html",
                            heading = "GLD Tweets",
                            gld_tweets = gld_tweets)

if __name__ == "__main__":
    app.run(port=7000,debug=True)