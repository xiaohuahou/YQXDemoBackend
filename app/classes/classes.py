#-*- coding: UTF-8 -*-
from flask import request, jsonify
from app.classes import classes
from app.database import db
import json

class Teacher(db.Document):
    name = db.StringField()

class Book(db.Document):
    title = db.StringField()
    author = db.DocumentField(Teacher)
    year = db.IntField()


@classes.route('/add', methods=['POST'])
def apidemo():
    """一个返回JSON数据接口的设计示例"""

    data = json.loads(request.data)

    author = Teacher(name=data['name'])
    author.save()

    jsonResponse = dict(errCode="1", errMsg="操作成功！")
    response = jsonify(jsonResponse)
    return response