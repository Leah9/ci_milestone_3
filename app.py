import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
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
@app.route("/get_terms")
def get_terms():
    terms = list(mongo.db.terms.find().sort("name"))
    print(terms)
    return render_template("terms.html", terms=terms)


@app.route("/")
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "warning")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!", "info")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash(f"Welcome, {request.form.get('username')}", "info")
                return redirect(url_for("get_terms"))
            else:
                # no match
                flash("Incorrect Username and/or Password", "warning")
                return redirect(url_for("login"))

        else:
            # username not found
            flash("Incorrect Username and/or Password", "warning")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out", "info")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_term", methods=["GET", "POST"])
def add_term():
    # On post create a dictionary then send it to the term table
    if request.method == "POST":
        term = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }
        # print(term)
        mongo.db.terms.insert_one(term)
        flash("Submitted, thank you!", "info")
        return redirect(url_for("get_terms"))
    # Default behavior
    return render_template(("add_term.html"))


@app.route("/edit_term/<term_id>", methods=["GET", "POST"])
def edit_term(term_id):
    # On post create a dictionary then send it to the term table
    if request.method == "POST":
        edited = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }
        print(edited)
        mongo.db.terms.replace_one({"_id": ObjectId(term_id)}, edited)
        flash("Updated, thank you!", "info")
        return redirect(url_for("get_terms"))
    # Default behavior
    # return render_template(("add_term.html"))

    term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    return render_template("edit_term.html", term=term)


@app.route("/delete_confirm/<term_id>")
def delete_confirm(term_id):
    term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    flash("WARNING", "warning")
    return render_template("delete_confirm.html", term=term)


@app.route("/delete_term/<term_id>")
def delete_term(term_id):
    mongo.db.terms.delete_one({"_id": ObjectId(term_id)})
    flash("Term deleted", "info")
    return redirect(url_for("get_terms"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
