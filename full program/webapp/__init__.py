from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_migrate import Migrate
import requests
import os


db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "VERY_STRONG_HASH"

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:&Shc>tdjRXx46=B@admin.cxq26ys6yxv9.us-east-1.rds.amazonaws.com:3306/main'
    db.init_app(app)

    @app.template_filter('random_img')
    def random_img(url):

        api_url = 'https://api.api-ninjas.com/v1/randomimage?category=technology'
        response = requests.get(api_url, headers={
                                'X-Api-Key': 'YOUR_API_KEY', 'Accept': 'image/jpg'}, stream=True)
        url = response.text

        print(url)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Phones

    if not os.path.exists('instance/test.db'):
        with app.app_context():
            db.create_all()
        print('db created')

    # migreate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
