#-*- coding: UTF-8 -*-
from flask import jsonify
from flask_restful import reqparse
from app.classes import classes
from app.database import db

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('_tid')

@classes.route('/classesAll', methods=['GET'])
def getClassAll():
    res = [c for c in db.classes.find({},{'_id' : False})]
    return jsonify({"result":"success", "data": res})

@classes.route('/classes', methods=['POST'])
def addClass():
    """add a class"""
    args = parser.parse_args()
    name = args.get('name') if args.get('name') else 'dummy class'
    _tid = args.get('_tid') if args.get('_tid') else 'dummy _tid'
    rid = db.classes.insert_one({'name': name, '_tid': _tid}).inserted_id
    return jsonify({"result":"success", "inserted_id": str(rid)})

@classes.route('/classes', methods=['PUT'])
def editClass():
    pass