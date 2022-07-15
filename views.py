from flask import render_template, redirect, url_for, Blueprint, request
# from app import app

my_view = Blueprint('my_view', __name__)

@my_view.route("/")    
def home():
    return render_template('index.html')

@my_view.route("/about")    
def about():
    return render_template('about.html')

@my_view.route("/rosaria")   # when the url is our_app/contact
def rosaria():
    return render_template('rosaria.html') #return contact.html

