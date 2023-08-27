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
    current_datetime = datetime.datetime.now()
    return render_template("offers.html", offers=offers,
                           current_datetime=current_datetime)


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
            "is_season": "off"
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
        {"username": username})

    if session["user"] == username:
        return render_template("profile.html", user=user)
    elif session["user"] and username != session["user"]:
        # preventing sensible data passed to front end.
        user2 = {
            "username": user["username"],
            "class_preference": user["class_preference"],
            "is_hardcore": user["is_hardcore"],
            "is_season": user["is_season"]
        }
        return render_template("profile.html", user=user2)
    else:
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
            "suffix": request.form.get("suffix"),
            "armor": int(request.form.get("armor", 0)),
            "damage": int(request.form.get("damage", 0)),
            "is_hardcore": is_hardcore,
            "is_season": is_season,
            "created_by": session["user"],
            "offer_price": request.form.get("offer_price"),
            "bids": [],
            "date": datetime.datetime.now(),
            "trade": {
                "user": "",
                "price": "",
                "traded_by_owner": "false",
                "traded_by_bidder": "false",
                "accepted": "false"
            }
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
        flash("Offer Successfully Added")
        return redirect(url_for("offers"))

    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template("add_offer.html", user=user, p_class=p_class,
                               item_types=item_types)
    else:
        flash("You must be logged in to create offer.")
        return render_template("login.html")


@app.route("/offer_info/<offer_id>", methods=["GET", "POST"])
def offer_info(offer_id):
    offer = mongo.db.offers.find_one({"_id": ObjectId(offer_id)})
    if request.method == "POST":
        if "user" in session:
            if request.form.get("offer_bid"):
                new_offer = {
                    "offer_bid": request.form.get("offer_bid"),
                    "user": session["user"],
                    "date": datetime.datetime.now()
                }

                offer["bids"].insert(0, new_offer)

                # use replace_one instead of update_one
                mongo.db.offers.replace_one({"_id": ObjectId(offer_id)}, offer)
                flash("Bid added")

            elif request.form.get("offer_accepted"):
                offer_accepted = {
                    "user": request.form.get("user"),
                    "price": request.form.get("price"),
                    "traded_by_owner": "false",
                    "traded_by_bidder": "false",
                    "accepted": request.form.get("offer_accepted")
                }
                offer["trade"] = offer_accepted
                mongo.db.offers.replace_one({"_id": ObjectId(offer_id)}, offer)

            elif request.form.get("traded_by_owner") or request.form.get("traded_by_bidder"):

                traded_by_owner = request.form.get(
                    "traded_by_owner") or offer["trade"]["traded_by_owner"]
                traded_by_bidder = request.form.get(
                    "traded_by_bidder") or offer["trade"]["traded_by_bidder"]

                offer_accepted = {
                    "user": offer["trade"]["user"],
                    "price": offer["trade"]["price"],
                    "traded_by_owner": traded_by_owner,
                    "traded_by_bidder": traded_by_bidder,
                    "accepted": offer["trade"]["accepted"]
                }
                offer["trade"] = offer_accepted
                mongo.db.offers.replace_one({"_id": ObjectId(offer_id)}, offer)

        else:
            flash("You must be logged in to place a bid.")
            return render_template("login.html")

    current_datetime = datetime.datetime.now()
    return render_template("offer_info.html", offer=offer,
                           current_datetime=current_datetime)


@app.route("/message/<reciever>", methods=["GET", "POST"])
def message(reciever):
    # grab the session user's user from db

    message_id = generate_combined_id(session["user"], reciever)

    user = mongo.db.users.find_one(
        {"username": session["user"]})

    message_data = mongo.db.messages.find_one(
        {"combined_id": message_id})

    current_datetime = datetime.datetime.now()

    # if message is being sent
    if request.method == "POST":

        new_message_data = {
            "user": session["user"],
            "message": request.form.get("message"),
            "discord_id": request.form.get("discord_id"),
            "b_net_id": request.form.get("b_net_id"),
            "date": datetime.datetime.now()
        }

        if message_data:
            message_data["messages"].append(new_message_data)
            new_message_array = message_data["messages"]

            updated_conversation = {
                "combined_id": message_data["combined_id"],
                "messages": new_message_array
            }
            mongo.db.messages.replace_one(
                {"_id": ObjectId(message_data["_id"])}, updated_conversation)
        else:
            new_conversation = {
                "combined_id": message_id,
                "messages": []
            }
            new_conversation["messages"].append(new_message_data)

            mongo.db.messages.insert_one(new_conversation)

        message_data = mongo.db.messages.find_one({"combined_id": message_id})

    return render_template("message.html", reciever=reciever,
                           message_data=message_data,
                           current_datetime=current_datetime, user=user)


# function takes 2 users and determines which name has higher
# value placing it first. Same Unique id is creted regardles with
# user is passed first keeping it consistent and dublicating records
def generate_combined_id(user1, user2):
    message_id = f"{max(user1, user2)}_{min(user1, user2)}"
    return message_id


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
