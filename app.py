import os
import json
import datetime
# sys used for calling print during the app runing
import sys
import pymongo
import itertools
#  print(variable, file = sys.stderr)
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

current_datetime = datetime.datetime.now()

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

    user = ""
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})

    check_notifications(user, False)
    return render_template("offers.html", offers=offers,
                           user=user, p_class=p_class, item_types=item_types,
                           current_datetime=current_datetime)


@app.route("/filter", methods=["GET", "POST"])
def filter():

    user = ""
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})

    check_notifications(user, False)

    is_hardcore = "on" if request.form.get("is_hardcore") else "off"
    is_season = "on" if request.form.get("is_season") else "off"
    affix_preference = []

    # affixes search sorted
    # making affixes lowercase
    for item in request.form.getlist("affix_preference"):
        affix_preference.append(item.lower())

    affix_range = int(request.form.get("affix_range"))

    # Creating unique combinations
    affix_combinations = list(
        itertools.combinations(affix_preference, affix_range))

    affix_queries = []

    for combo in affix_combinations:
        affix_queries.append({"affix_array": {"$all": list(combo)}})

    search_paramaters = {
        "class_preference": request.form.get("class_preference"),
        "item_preference": request.form.get("item_preference"),
        "is_hardcore": is_hardcore,
        "is_season": is_season,
    }

    search_query = {
        "$and": [
            {"class_data": search_paramaters["class_preference"]},
            {"item_data": search_paramaters["item_preference"]},
            {"$or": affix_queries},
            {"is_hardcore": search_paramaters["is_hardcore"]},
            {"is_season": search_paramaters["is_season"]},
        ]
    }

    results = list(mongo.db.offers.find(search_query))

    return render_template("offers.html", offers=results,
                           user=user, p_class=p_class, item_types=item_types,
                           current_datetime=current_datetime)


@ app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # takes users details
        username = request.form.get("username")
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
            "is_season": "off",
            "message_count": 0,
            "trades_completed": 0
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username")
        session["messages"] = 0
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@ app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username")
                flash("Welcome, {}".format(
                    request.form.get("username")))
                session["messages"] = 0
                check_notifications("", True)
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


@ app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    user = mongo.db.users.find_one(
        {"username": username})

    offers = list(mongo.db.offers.find({"created_by": username}))

    if session["user"]:
        if session["user"] == username:
            check_notifications(user, False)
            return render_template("profile.html", user=user, offers=offers,
                                current_datetime=current_datetime)
        else:
            # preventing sensible data passed to front end.
            user2 = {
                "username": user["username"],
                "class_preference": user["class_preference"],
                "is_hardcore": user["is_hardcore"],
                "is_season": user["is_season"]
            }
            check_notifications(user, False)
            return render_template("profile.html", user=user2, offers=offers,
                                current_datetime=current_datetime)
    else:
        return redirect(url_for("login"))


@ app.route("/edit_profile/<username>", methods=["GET", "POST"])
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
            "is_season": is_season,
            "message_count": user["message_count"]
        }
        mongo.db.users.replace_one({"_id": ObjectId(user["_id"])}, submit)
        user2 = mongo.db.users.find_one({"_id": ObjectId(user["_id"])})
        flash("Profile Successfully Updated")
        check_notifications(user, False)
        return render_template("profile.html", user=user2)

    if session["user"]:
        check_notifications(user, False)
        return render_template("edit_profile.html", user=user, p_class=p_class)

    return redirect(url_for("register"))


@ app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    session.pop("messages")
    return redirect(url_for("login"))


@ app.route("/add_offer", methods=["GET", "POST"])
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
            "date": current_datetime,
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
        affix_array = []

        # Capture any additional form keys dynamically and store in affixes
        for key in request.form.keys():
            if key not in offer:
                affixes[key] = request.form.getlist(key)[0]
                affix_array.append(key.replace('-', ' '))

        # Add affixes to the offer dictionary if there are any
        if affixes or affix_array:
            offer["affixes"] = affixes
            offer["affix_array"] = affix_array

        mongo.db.offers.insert_one(offer)
        flash("Offer Successfully Added")
        return redirect(url_for("offers"))

    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        check_notifications(user, False)
        return render_template("add_offer.html", user=user, p_class=p_class,
                               item_types=item_types)
    else:
        flash("You must be logged in to create offer.")
        return render_template("login.html")


@ app.route("/offer_info/<offer_id>", methods=["GET", "POST"])
def offer_info(offer_id):
    offer = mongo.db.offers.find_one({"_id": ObjectId(offer_id)})

    if request.method == "POST":
        if "user" in session:
            if request.form.get("offer_bid"):
                new_offer = {
                    "offer_bid": request.form.get("offer_bid"),
                    "user": session["user"],
                    "date": current_datetime
                }

                offer["bids"].insert(0, new_offer)

                # use replace_one instead of update_one
                mongo.db.offers.replace_one({"_id": ObjectId(offer_id)}, offer)
                flash("Bid added")

            elif request.form.get("accepted"):
                offer_accepted = {
                    "user": request.form.get("user"),
                    "price": request.form.get("price"),
                    "traded_by_owner": "false",
                    "traded_by_bidder": "false",
                    "accepted": request.form.get("accepted")
                }
                offer["trade"] = offer_accepted
                mongo.db.offers.replace_one({"_id": ObjectId(offer_id)}, offer)

                # calls function to send a message of bid accepted
                message_bid_accepted(
                    offer_accepted["user"], offer_accepted["price"], offer)

                return redirect(url_for("message",
                                        reciever=offer_accepted["user"]))

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
                if offer_accepted["traded_by_owner"] == "true" and offer_accepted["traded_by_bidder"] == "true":
                    mongo.db.offers.delete_one({"_id": ObjectId(offer_id)})

                    # add trade score to users
                    owner = mongo.db.users.find_one(
                        {"username": offer["created_by"]})
                    bidder = mongo.db.users.find_one(
                        {"username": offer_accepted["user"]})

                    owner["trades_completed"] += 1
                    bidder["trades_completed"] += 1

                    mongo.db.users.replace_one(
                        {"_id": ObjectId(owner["_id"])}, owner)
                    mongo.db.users.replace_one(
                        {"_id": ObjectId(bidder["_id"])}, bidder)

                    flash("Item is fully traded and deleted from database")
                    return redirect(url_for("offers"))
                else:
                    mongo.db.offers.replace_one(
                        {"_id": ObjectId(offer_id)}, offer)

        else:
            flash("You must be logged in to place a bid.")
            return render_template("login.html")

    check_notifications("", True)
    return render_template("offer_info.html", offer=offer,
                           current_datetime=current_datetime)


@app.route("/delete_offer/<offer_id>")
def delete_offer(offer_id):
    mongo.db.offers.delete_one({"_id": ObjectId(offer_id)})
    flash("Offer Successfully Deleted")
    return redirect(url_for("offers"))


@ app.route("/messages/<username>")
def messages(username):
    # grab the session user's user from db
    chat_list = list(mongo.db.messages.find(
        {"$text": {"$search": session["user"]}}))

    # Sort chat_list based on the most recent message in each chat
    sorted_chat_list = sorted(
        chat_list,
        key=lambda chat: chat['messages'][-1]['date'],
        reverse=True
    )
    check_notifications("", True)
    return render_template("messages.html", chat_list=sorted_chat_list,
                           current_datetime=current_datetime)


@ app.route("/message/<reciever>", methods=["GET", "POST"])
def message(reciever):

    # generate message id for a chat
    message_id = generate_combined_id(session["user"], reciever)
    message_data = mongo.db.messages.find_one(
        {"combined_id": message_id})

    user = mongo.db.users.find_one(
        {"username": session["user"]})
    other_user = mongo.db.users.find_one(
        {"username": reciever})

    if message_data:
        # find out which user is user1 and 2 and update unread message count
        if session["user"] == message_data["user1"]:
            user["message_count"] -= message_data["user1_unread"]
            message_data["user1_unread"] = 0
            user1_count = 0
            user2_count = message_data["user2_unread"] + 1
        else:
            user["message_count"] -= message_data["user2_unread"]
            message_data["user2_unread"] = 0
            user1_count = message_data["user1_unread"] + 1
            user2_count = 0

    # Updates user message score
    mongo.db.users.replace_one(
        {"_id": ObjectId(user["_id"])}, user)

    # if message is being sent first of check if conversation was started,
    # if not starts new
    if request.method == "POST":

        new_message_data = {
            "user": session["user"],
            "message": request.form.get("message"),
            "discord_id": request.form.get("discord_id"),
            "b_net_id": request.form.get("b_net_id"),
            "date": current_datetime,
        }

        # updates another user personal score for read
        # messages and session info
        other_user["message_count"] += 1
        mongo.db.users.replace_one(
            {"_id": ObjectId(other_user["_id"])}, other_user)

        if message_data:
            message_data["messages"].append(new_message_data)
            new_message_array = message_data["messages"]

            updated_conversation = {
                "combined_id": message_data["combined_id"],
                "user1": message_data["user1"],
                "user1_unread": user1_count,
                "user2": message_data["user2"],
                "user2_unread":  user2_count,
                "messages": new_message_array
            }
            mongo.db.messages.replace_one(
                {"_id": ObjectId(message_data["_id"])}, updated_conversation)

        else:
            new_conversation = {
                "combined_id": message_id,
                "user1": session["user"],
                "user1_unread": 0,
                "user2": reciever,
                "user2_unread": 1,
                "messages": [new_message_data]
            }

            mongo.db.messages.insert_one(new_conversation)

        message_data = mongo.db.messages.find_one({"combined_id": message_id})

        # in case of just loading the screen it updates
        # the unread message count
    else:
        if message_data:
            mongo.db.messages.replace_one(
                {"_id": ObjectId(message_data["_id"])}, message_data)

    check_notifications(user, False)
    return render_template("message.html", reciever=reciever,
                           message_data=message_data,
                           current_datetime=current_datetime, user=user)


# function takes bid-acceptence details and creates new message.
# used in "@app.route offer_info"
def message_bid_accepted(reciever, bid, offer):
    # generate message id for a chat
    message_id = generate_combined_id(session["user"], reciever)
    message_data = mongo.db.messages.find_one(
        {"combined_id": message_id})

    user = mongo.db.users.find_one(
        {"username": session["user"]})
    other_user = mongo.db.users.find_one(
        {"username": reciever})

    other_user["message_count"] += 1
    mongo.db.users.replace_one(
        {"_id": ObjectId(other_user["_id"])}, other_user)

    if message_data:
        # find out which user is user1 and 2 and update unread message count
        if session["user"] == message_data["user1"]:
            user["message_count"] -= message_data["user1_unread"]
            message_data["user1_unread"] = 0
            user1_count = 0
            user2_count = message_data["user2_unread"] + 1
        else:
            user["message_count"] -= message_data["user2_unread"]
            message_data["user2_unread"] = 0
            user1_count = message_data["user1_unread"] + 1
            user2_count = 0

    offer = mongo.db.offers.find_one({"_id": ObjectId(offer["_id"])})

    new_message_data = {
        "user": session["user"],
        "message": "",
        "discord_id": "",
        "b_net_id": "",
        "date": current_datetime,
        "offer_accepted": {
            "bid": bid,
            "offer_id": offer["_id"],
            "offer_name": offer["item_data"]
        }
    }

    if message_data:
        message_data["messages"].append(new_message_data)
        new_message_array = message_data["messages"]

        updated_conversation = {
            "combined_id": message_data["combined_id"],
            "user1": message_data["user1"],
            "user1_unread": user1_count,
            "user2": message_data["user2"],
            "user2_unread":  user2_count,
            "messages": new_message_array
        }
        mongo.db.messages.replace_one(
            {"_id": ObjectId(message_data["_id"])}, updated_conversation)
    else:
        new_conversation = {
            "combined_id": message_id,
            "user1": session["user"],
            "user1_unread": 0,
            "user2": reciever,
            "user2_unread": 1,
            "messages": [new_message_data]
        }

        mongo.db.messages.insert_one(new_conversation)

    message_data = mongo.db.messages.find_one({"combined_id": message_id})


# function check the active sesion["user"] and checks active messages from
# server user profile to update session count this function called at
# every loading screen to have up to date message count. Some functions
# will already call user some will not, allowing for both options
# to reduce loading times
def check_notifications(user, check):
    if "user" in session:
        if check:
            user = mongo.db.users.find_one(
                {"username": session["user"]})

        session["messages"] = user["message_count"]

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
