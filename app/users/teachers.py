#-*- coding: UTF-8 -*-
from flask import request, jsonify
from app.users import users

@users.route('/teachers', methods=['GET'])
def getTeacher():
    """一个返回JSON数据接口的设计示例"""
    pass

@users.route('/teachers', methods=['POST'])
def addTeacher():
    """一个返回JSON数据接口的设计示例"""
    pass


@users.route('/teachers', methods=['PUT'])
def editTeacher():
    """一个返回JSON数据接口的设计示例"""
    pass