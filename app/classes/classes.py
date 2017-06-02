#-*- coding: UTF-8 -*-
from flask import request, jsonify
from app.classes import classes
import json

@classes.route('/classes', methods=['GET'])
def getClass():
    pass

@classes.route('/classes', methods=['POST'])
def addClass():
    """一个返回JSON数据接口的设计示例"""

    data = json.loads(request.data)

    jsonResponse = dict(errCode="1", errMsg="操作成功！")
    response = jsonify(jsonResponse)
    return response

@classes.route('/classes', methods=['PUT'])
def editClass():
    pass