import os
import json
import datetime
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

# ------------------------------------------------------------------------------
# turning json data in to item data
# file_path = 'item_data.json'
# with open(file_path, 'r') as json_file:
#     json_data = json_file.read()

# parsed_data = json.loads(json_data)

# print(parsed_data["Helm"]["affixes"]["all_classes"][2])
# -----------------------------------------------------------------------------

# page specific variables
# these are stable and does not require its own database
p_class = ["All Classes", "Barbarian", "Druid",
           "Necromancer", "Rogue", "Sorcerer"]

item_types = ["Helm", "Chest Armor", "Gloves", "Pants", "Boots", "Amulet",
              "Ring", "1h Sword", "1h Axe", "1h Mace", "Dagger", "1h Scythe",
              "Wand", "2h Sword", "2h Axe", "2h Mace", "Polearm", "Bow",
              "Crossbow", "2h Scythe", "Staff", "Offhand", "Shield"]


@app.route("/")
@app.route("/offers")
def offers():
    offers = list(mongo.db.offers.find())
    return render_template("offers.html", offers=offers)


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
        is_season = "on" if request.form.get("is_season") else "off"
        submit = {
            "username": user["username"],
            "password": user["password"],
            "b_net_id": request.form.get("b_net_id"),
            "discord_id": request.form.get("discord_id"),
            "class_preference": request.form.get("class_preference"),
            "is_hardcore": is_hardcore,
            "is_season": is_season
        }
        mongo.db.users.replace_one({"_id": ObjectId(user["_id"])}, submit)
        user2 = mongo.db.users.find_one({"_id": ObjectId(user["_id"])})
        flash("Profile Successfully Updated")
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


@app.route("/add_offer", methods=["GET", "POST"])
def add_offer():
    if request.method == "POST":
        is_hardcore = "on" if request.form.get("is_hardcore") else "off"
        is_season = "on" if request.form.get("is_season") else "off"

        offer = {
            "class_data": request.form.get("class_data"),
            "item_data": request.form.get("item_data"),
            "suffix-data": request.form.get("suffix_data"),
            "armor": request.form.get("armor", 0),
            "damage": request.form.get("damge", 0),
            "is_hardcore": is_hardcore,
            "is_season": is_season,
            "created_by": session["user"]
        }

        # Create a list to store unknown key-value pairs
        affixes = {}

        # Capture any additional form keys dynamically and store in affixes
        for key in request.form.keys():
            if key not in offer:
                affixes[key] = request.form.getlist(key)[0]

        # Add affixes to the offer dictionary if there are any
        if affixes:
            offer["affixes"] = affixes

        mongo.db.offers.insert_one(offer)
        flash("Task Successfully Added")
        return redirect(url_for("offers"))

    user = mongo.db.users.find_one(
        {"username": session["user"]})
    return render_template("add_offer.html", user=user, p_class=p_class,
                           item_types=item_types)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
