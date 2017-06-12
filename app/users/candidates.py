#-*- coding: UTF-8 -*-
from flask import jsonify
from flask_restful import reqparse
from app.classes import classes
from app.database import db

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('_tid')

# to add class signup contact information
@classes.route('/candidate', methods=['POST'])
def addClass():
    pass
