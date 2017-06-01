#-*- coding: UTF-8 -*-
from flask import request, jsonify
from app.classes import classes
from app.database import db
import json



class Class(db.Document):
    title = db.StringField()
    teacher = db.DocumentField(Teacher)
    studentNum = db.IntField()

@classes.route('/api/v1/class', methods=['GET'])
def getClass():
    pass

@classes.route('/api/v1/class', methods=['POST'])
def addClass():
    """一个返回JSON数据接口的设计示例"""

    data = json.loads(request.data)

    author = Teacher(name=data['name'])
    author.save()

    jsonResponse = dict(errCode="1", errMsg="操作成功！")
    response = jsonify(jsonResponse)
    return response



@classes.route('/api/v1/class', methods=['PUT'])
def editClass():
    pass