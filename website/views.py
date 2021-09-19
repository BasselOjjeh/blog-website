from flask import Blueprint, render_template

views = Blueprint("views", __name__)

#Setting Up a Blueprint using Jinja
@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")
