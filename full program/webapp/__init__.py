from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import requests
import os
from flask_restful import Api



db = SQLAlchemy()
app = Flask(__name__)
api = Api(app)


def create_app():

    app.config['SECRET_KEY'] = "VERY_STRONG_HASH"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main_data.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:&Shc>tdjRXx46=B@admin.cxq26ys6yxv9.us-east-1.rds.amazonaws.com:3306/main'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .api import api_blue

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(api_blue, url_prefix="/api")

    from .models import User, Phones

    # if not os.path.exists('instance/test.db'):
    #     with app.app_context():
    #         db.create_all()
    #     print('db created')

    migreate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
