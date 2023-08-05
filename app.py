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

# page specific variables
# these are stable and does nto require its own database
p_class = ["None", "Barbarian", "Druid",
           "Necromancer", "Rogue", "Sorcerer"]


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

        # Saving user to database and filling with default values
        register = {
            "username": username,
            "password": hashed_password,
            "b_net_id": "",
            "discord_id": "",
            "class_preference": "None",
            "is_hardcore": "off",
            "is_ladder": "off"
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if session["user"]:
        return render_template("profile.html", user=user)

    return redirect(url_for("login"))


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    # grab the session user's user from db
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    # if user is being eddited
    if request.method == "POST" and session["user"]:
        is_hardcore = "on" if request.form.get("is_hardcore") else "off"
        is_seasson = "on" if request.form.get("is_seasson") else "off"
        submit = {
            "username": user["username"],
            "password": user["password"],
            "b_net_id": request.form.get("b_net_id"),
            "discord_id": request.form.get("discord_id"),
            "class_preference": request.form.get("class_preference"),
            "is_hardcore": is_hardcore,
            "is_seasson": is_seasson
        }
        mongo.db.users.replace_one({"_id": ObjectId(user["_id"])}, submit)
        user2 = mongo.db.users.find_one({"_id": ObjectId(user["_id"])})
        flash("Task Successfully Updated")
        return render_template("profile.html", user=user2)

    if session["user"]:
        return render_template("edit_profile.html", user=user, p_class=p_class)

    return redirect(url_for("register"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
