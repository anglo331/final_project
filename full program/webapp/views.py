from flask import Blueprint, render_template

views = Blueprint("views",__name__)

@views.route("/")
def home():
    return render_template('home.html')

@views.route('/product.html')
def product():
    return render_template('/product.html')