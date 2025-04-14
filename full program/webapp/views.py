from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Phones
from . import db
# from .ai import simplechat


views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    items = Phones.query.paginate(page=page, per_page=12)
    return render_template('home.html', user=current_user, itmes=items)


@views.route('/product/<int:id>')
def product(id):
    itme = Phones.query.filter_by(id=id).first()
    discreption = ''
    if itme.img_url:
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


@views.route('/chat', methods=['GET', "POST"])
def chat():
    if request.method == 'GET':
        msg = request.form.get("msg")
        answer = simplechat(msg)

        res =[
            {'role': 'user', 'massage': msg},
            {'role': 'ai', 'massage': answer}]

        return render_template('chat.html', respons=res, user=current_user)

    return render_template('chat.html', user=current_user)

