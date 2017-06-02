#-*- coding: UTF-8 -*-
from flask import request
from bson.json_util import dumps
from bson.objectid import ObjectId
from app.database import db
from app.users import users


@users.route('/teachers', methods=['GET'])
def getTeacher():
    teachers = db.teachers.find()
    return dumps(teachers)


@users.route('/teachers', methods=['POST'])
def addTeacher():
    name = request.args.get('name', '')
    db.teachers.insert_one({
        'name': name
    })
    return "Success"


@users.route('/teachers/<string:teacher_id>', methods=['PUT'])
def editTeacher(teacher_id):
    name = request.args.get('name', '')
    db.teachers.update_one({'_id': ObjectId(teacher_id)},
                           {'$set': {'name': name}})
    return "Success"