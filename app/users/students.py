#-*- coding: UTF-8 -*-
from flask import request, jsonify
from flask_restful import reqparse
from bson import ObjectId
from app.database import db
from app.users import users

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('_cid', action='append')


@users.route('/students', methods=['GET'])
def getStudentAll():
    res = [t for t in db.students.find({}, {'_id': False})]
    return jsonify({
        'result': 'success',
        'data': res
    })


@users.route('/students', methods=['POST'])
def addStudent():
    args = parser.parse_args()
    name = args.get('name')
    _cid = args.get('_cid')

    if name and _cid:
        rid = db.students.insert_one({
            'name': name,
            'classes': [{'_cid': c} for c in _cid]
        }).inserted_id
        return jsonify({
            'result': 'success',
            'inserted_id': str(rid)
        })
    else:
        return jsonify({
            'error': 'Name or _cid blank'
        })


@users.route('/students/<string:something>', methods=['PUT'])
def editStudent(something):
    pass
