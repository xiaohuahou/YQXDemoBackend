#-*- coding: UTF-8 -*-
from flask import request, jsonify
from app.users import users
from app.database import db


class Teacher(db.Document):
    name = db.StringField()
    profile = db.StringField()
    img = db.StringField()


@users.route('/api/v1/teacher', methods=['GET'])
def getTeacher():
    """一个返回JSON数据接口的设计示例"""
    pass

@users.route('/api/v1/teacher', methods=['POST'])
def addTeacher():
    """一个返回JSON数据接口的设计示例"""
    pass


@users.route('/api/v1/teacher', methods=['PUT'])
def editTeacher():
    """一个返回JSON数据接口的设计示例"""
    pass