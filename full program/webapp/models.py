from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    u_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    joining_date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f'<{self.id=}, {self.f_name=}, {self.email}, {self.joining_date}>'


class Phones(db.Model):
    __tablename__ = 'Phones'

    id = db.Column(db.Integer, primary_key=True)
    Brand = db.Column(db.String(100))
    model_name = db.Column(db.String(100))
    seller = db.Column(db.String(225))
    Storage_in_GB = db.Column(db.Integer)
    RAM = db.Column(db.Integer)
    Screen_Size_inches = db.Column(db.Float)
    Camera = db.Column(db.String(100))
    Battery_capacity = db.Column(db.Integer)
    current_price = db.Column(db.Integer)
    img_url = db.Column(db.String(225))
    relations = db.relationship('price_history')

    def __repr__(self):
        return f'<{self.id=}, {self.model_name=}, {self.price=}LE>'


class price_history (db.Model):
    __tablename__ = 'price_history'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('Phones.id'), nullable=False)
    saller = db.Column(db.String(100), nullable=False)
    old_price = db.Column(db.Integer)
    new_price = db.Column(db.Integer)
    change_date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f'<{self.item_id=}, {self.old_price=}, {self.new_price=}, {self.change_date=}>'
