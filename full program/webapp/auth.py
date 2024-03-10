from flask import Blueprint, render_template, request
from .classes import *

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    anglo = user()
    if True == anglo.email:
        print("valid user")
    return render_template('login.html')


@auth.route("/singup")
def singup():
    return render_template('singup.html')
