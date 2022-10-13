"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os, urllib.parse
from flask import Flask, request, jsonify, url_for, Blueprint, redirect
from api.models import db, User, Message, Vehicle, Business, Booking
from api.utils import generate_sitemap, APIException
from werkzeug.security import check_password_hash, generate_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, decode_token
# from flask_jwt_extended import JWTManager
from sqlalchemy import or_, exc
from dotenv import load_dotenv

api = Blueprint('api', __name__)
load_dotenv()
app = Flask(__name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route("/signup", methods=["POST"])
def createNewUser():
    request_body = request.get_json(force=True)
    email = request_body['email']
    name = request_body['name']
    password = request_body['password']
    hash_password = generate_password_hash(password)
    is_active = True

    try:
        user = User(email=email, name=name, password=hash_password, is_active=is_active)
    except exc.SQLAlchemyError: 
        return jsonify("error creating the user"), 400
    try:
        db.session.add(user)
    except exc.SQLAlchemyError: 
        return jsonify("error adding the user"), 400
    db.session.commit()

    access_token = create_access_token(identity=email)
    # send_welcome_email(user)
    return jsonify({"msg": "sign up complete", "access_token" : access_token}), 201

    # except SQLAlchemyError: 
    #     return jsonify({"msg": "user already exists"}), 400
        
    #     pass

    return jsonify({"msg": "error signing up"}), 401

# id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), unique=True, nullable=False)
#     surname = db.Column(db.String(120), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)
#     lister = db.Column(db.Boolean(), unique=False, nullable=True)
#     phone_number = db.Column(db.String(40), unique=True, nullable=True)


if __name__ == "__main__":
    app.run(debug=True)