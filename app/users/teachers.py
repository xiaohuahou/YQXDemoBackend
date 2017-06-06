#-*- coding: UTF-8 -*-
from flask import request, jsonify
from flask_restful import reqparse
from bson import ObjectId
from app.database import db
from app.users import users

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help='Name cannot be blank')


@users.route('/teachers', methods=['GET'])
def getTeacher():
    res = [t for t in db.teachers.find({}, {'_id': False})]
    return jsonify({
        'result': 'success',
        'data': res
    })


@users.route('/teachers', methods=['POST'])
def addTeacher():
    args = parser.parse_args()
    name = args.get('name')
    if name:
        rid = db.teachers.insert_one({
            'name': name
        }).inserted_id
        return jsonify({
            'result': 'success',
            'inserted_id': str(rid)
        })
    else:
        return jsonify({
            'error': 'Name cannot be blank'
        })


@users.route('/teachers/<string:teacher_id>', methods=['PUT'])
def editTeacher(teacher_id):
    args = parser.parse_args()
    name = args.get('name')
    if args.get('name'):
        db.teachers.update_one({'_id': ObjectId(teacher_id)},
                               {'$set': {'name': name}})
        return jsonify({
            'result': 'success'
        })
    else:
        return jsonify({
            'error': 'ID does not exist'
        })
