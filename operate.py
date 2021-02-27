# -*- encoding: utf-8 -*-
"""
@File    :   operate.py
@Contact :   codeboycb@gmail.com
@License :   (C)Copyright 2020-present,Guan Yongjie 官咏颉
"""
import datetime
from sqlalchemy import or_, and_
from flask import jsonify, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import flag_modified

import orm


def UserRegister(username, password, email, invitation=''):
    response = {}
    Session = sessionmaker(bind=orm.engine)
    # 创建 Session 类实例
    session1 = Session()
    count = session1.query(orm.Users).filter(orm.Users.email == email).count()
    if count == 0:
        # 新增
        user = orm.Users(username=username,
                         email=email,
                         invitation=invitation
                         )
        user.set_password(password)
        # 保存
        session1.add(user)
        # 提交
        session1.commit()
        session1.flush()
        newid = user.id
        session1.close()
        response['res'] = "注册成功"
        session['userid'] = newid
        session.permanent = True  # 长期有效，一个月的时间有效
        return jsonify(response), 200
    else:
        session1.close()
        response['res'] = "用户已存在"
        return jsonify(response), 400


def UserLogin(email, password):
    response = {}
    Session = sessionmaker(bind=orm.engine)
    # 创建 Session 类实例
    session1 = Session()

    user = session1.query(orm.Users).filter(orm.Users.email == email).first()
    # 关闭
    session1.close()
    if user.check_password(password):
        response['res'] = "登录成功"
        session['userid'] = user.id
        session.permanent = True  # 长期有效，一个月的时间有效
        return jsonify(response), 200
    else:
        response['res'] = "用户名和密码不匹配"
        return jsonify(response), 400


def SubmitTest(examid, answer):
    response = {}
    Session = sessionmaker(bind=orm.engine)
    # 创建 Session 类实例
    session1 = Session()
    count = session1.query(orm.testRecord).filter(
        and_(orm.testRecord.userid == session.get('userid'), orm.testRecord.examid == examid)).count()
    if count == 0:
        # 新增
        record = orm.testRecord(userid=session.get('userid'),
                                examid=examid,
                                answer=answer
                                )
        # 保存
        session1.add(record)
        # 提交
        session1.commit()
        session1.close()
        response['res'] = "提交成功"
        return jsonify(response), 200
    else:
        record = session1.query(orm.testRecord).filter(
            and_(orm.testRecord.userid == session.get('userid'), orm.testRecord.examid == examid)).first()
        record.answer = answer
        # 保存
        session1.add(record)
        # 提交
        session1.commit()
        session1.close()
        response['res'] = "保存成功"
        return jsonify(response), 200


def getBookContent(bookid):
    response = {}
    Session = sessionmaker(bind=orm.engine)
    # 创建 Session 类实例
    session1 = Session()

    if session1.query(orm.Books).filter(orm.Books.id == bookid) == 1:
        book = session1.query(orm.Books).filter(orm.Books.id == bookid).first()
        response['data'] = book
        response['res'] = "查询成功"
        session1.close()
        return jsonify(response), 200
    else:
        response['res'] = "没有此书"
        session1.close()
        return jsonify(response), 400


def uploadBook(name, content, seriesid=0, isprivate=0, classid=None):
    response = {}
    Session = sessionmaker(bind=orm.engine)
    # 创建 Session 类实例
    session1 = Session()

    # 新增
    book = orm.Books(name=name,
                     content=content,
                     seriesid=seriesid,
                     isprivate=isprivate,
                     classid=classid
                     )
    session1.add(book)
    session1.flush()
    newid = book.id
    # 提交
    session1.commit()
    session1.close()
    response['res'] = "上传成功"
    response['data'] = {'id': newid}
    return jsonify(response), 200

