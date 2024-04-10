from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Phones



views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    items = Phones.query.all()
    return render_template('home.html', user=current_user, itmes=items)


@views.route('/product/<int:id>')
def product(id):
    itme = Phones.query.filter_by(id=id).first()
    if itme.img_url :
        imgs = [url for url in itme.img_url.split("'") if len(url.strip()) > 1]
        return render_template('/product.html', urls=imgs, item=itme, user=current_user)
    else:
        return render_template('/product.html', urls=['https://e7.pngegg.com/pngimages/440/997/png-clipart-feature-phone-mobile-phone-accessories-mobile-device-pattern-phone-gadget-phone-icon-thumbnail.png'], item=itme, user=current_user)


@views.route('/profile')
@login_required
def profile():
    return render_template('/profile.html', user=current_user)

@views.route('/features')
def features():
    return render_template('/features.html', user=current_user)

@views.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', user=current_user)

