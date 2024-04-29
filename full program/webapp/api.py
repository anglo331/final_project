from flask import Blueprint, request
from flask_restful import Resource, reqparse, fields, marshal_with
from .models import Phones, price_history
from . import db, api


api_blue = Blueprint('api', __name__)

phone_args = reqparse.RequestParser()

phone_args.add_argument(
    'Brand', type=str, help='Phone brand is missing please enter phone brand like [ samsung, apple, etc.]')
phone_args.add_argument(
    'model_name', type=str, help='Phone model is missing please enter phone model')
phone_args.add_argument(
    'color', type=str, help='Phone color is missing please enter phone model')
phone_args.add_argument(
    'seller', type=str, help='Phone seller is missing please enter phone seller like [ amazon, noon, etc.]')
phone_args.add_argument('Storage_in_GB', type=int,
                        help='Phone storage size is missing ')
phone_args.add_argument(
    'RAM', type=int, help='Phone memorey (ram) size is missing ')
phone_args.add_argument('screen_size', type=float,
                        help='Phone screen size is missing ')
phone_args.add_argument(
    'Camera', type=str, help='Phone cameras info is missing ')
phone_args.add_argument('Battery_capactiy', type=int,
                        help='Phone battery capacity is missing ')
phone_args.add_argument('current_price', type=int,
                        help='Phone price is missing ')
phone_args.add_argument('product_url', type=int,
                        help='Phone product_url is missing ')
phone_args.add_argument('img_url', type=int,
                        help='Phone img_url is missing ')


represent_data = {
    'id': fields.Integer,
    'Brand': fields.String,
    'model_name': fields.String,
    'color': fields.String,
    'seller': fields.String,
    'Storage_in_GB': fields.Integer,
    'RAM': fields.Integer,
    'Screen_Size_inches': fields.Float,
    'Camera': fields.String,
    'Battery_capactiy': fields.Integer,
    'current_price': fields.Integer,
    'product_url': fields.String,
    'img_url': fields.List,
}


class add (Resource):

    @marshal_with(represent_data)
    def put(self):
        args = phone_args.parse_args()
        if Phones.query.filter_by(Brand=args['Brand'], model_name=args['model_name'], saller=args['saller']).first():
            return 409, {'massage': "the phone aredy exist!!"}
        else:
            phone = Phones(Brand=args['Brand'],
                           model_name=args['model_name'],
                           saller=args['saller'],
                           Storage_in_GB=args['Storage_in_GB'],
                           RAM=args['RAM'],
                           Screen_Size_inches=args['Screen_Size_inches'],
                           Camera=args['Camera'],
                           Battery_capactiy=args['Battery_capactiy'],
                           product_url=args['product_url'],
                           img_url=args['img_url']
                           )
            db.session.add(phone)
            db.session.commit()
            return phone


api.add_resource(add, '/api/add')
