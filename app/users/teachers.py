#-*- coding: UTF-8 -*-
from flask import request, jsonify
from flask_restful import reqparse
from bson import ObjectId
from app.database import db
from app.users import users

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('_tid')


@users.route('/teachers', methods=['GET'])
def getTeacherAll():
    res = [t for t in db.teachers.find({}, {'_id': False})]
    return jsonify({
        'result': 'success',
        'data': res
    })


@users.route('/teachers', methods=['POST'])
def addTeacher():
    args = parser.parse_args()
    name = args.get('name')
    _tid = args.get('_tid')

    if name and _tid:
        rid = db.teachers.insert_one({
            'name': name,
            '_tid': _tid
        }).inserted_id
        return jsonify({
            'result': 'success',
            'inserted_id': str(rid)
        })
    else:
        return jsonify({
            'error': 'Name or _tid blank'
        })


@users.route('/teachers/<string:teacher_id>', methods=['PUT'])
def editTeacher(teacher_id):
    args = parser.parse_args()
    name = args.get('name')
    _tid = args.get('_tid')

    if args.get('name'):
        db.teachers.update_one({'_id': ObjectId(teacher_id)},
                               {'$set': {
                                   'name': name,
                                   '_tid': _tid
                               }})
        return jsonify({
            'result': 'success'
        })
    else:
        return jsonify({
            'error': 'ID does not exist'
        })
