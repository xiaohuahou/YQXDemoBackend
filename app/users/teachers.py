#-*- coding: UTF-8 -*-
from flask import request, jsonify
from app.users import users

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