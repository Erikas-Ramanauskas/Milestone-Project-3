import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/offers")
def offers():
    offers = list(mongo.db.offers.find())
    return render_template("offers.html", offers=offers)

# @app.route("/")
# @app.route("/requests")
# def requests():
#     requests = list(mongo.db.requests.find())
#     return render_template("requests.html", requests=requests)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # takes users details
        username = request.form.get("username").lower()
        password = request.form.get("password")
        r_password = request.form.get("r_password")

        # Checkign for mathcing Passwords
        if password != r_password:
            flash("Passwords do not match")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        # Saving user to database
        register = {
            "username": username,
            "password": hashed_password
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)