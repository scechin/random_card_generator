"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db
from api.utils import generate_sitemap
import random
#from models import Person

api = Blueprint('api', __name__)


@api.route('/card', methods=['GET'])
def get_card():

    suites = ["Spades","Hearts","Clubs","Diamonds"]
    values = ["ace", "king", "queen", "jacks", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    random_suites_position = random.randint(0, 3)
    random_values_position = random.randint(0,12)
    
    body = {
        "suit": suites[random_suites_position],
        "number": values[random_values_position]
    }

    return jsonify(body), 200