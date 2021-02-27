# -*- encoding: utf-8 -*-
"""
@File    :   orm.py    
@Contact :   codeboycb@gmail.com
@License :   (C)Copyright 2020-present,Guan Yongjie 官咏颉 
"""
from datetime import date, datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Date, Boolean, create_engine, JSON
from werkzeug.security import generate_password_hash, check_password_hash

# 映射基类
Base = declarative_base()
engine = create_engine('mysql+mysqldb://root:密码@localhost:3306/ris?charset=utf8',
                       echo=True,
                       pool_size=10,
                       pool_recycle=3600)
conn = engine.connect()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    phone = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    pswd = Column(String(1023), nullable=False)
    classid = Column(Integer)
    joindate = Column(DateTime, nullable=False,
                      default=datetime.utcnow)
    birthday = Column(Date)
    teacher = Column(Boolean, default=False)
    invitation = Column(String(255))

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)

    def set_password(self, password):
        self.pswd = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pswd, password)


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True, nullable=False)
    content = Column(String(5011))
    seriesid = Column(Integer)
    classid = Column(Integer, default=0)
    isprivate = Column(Boolean, default=False)
    practice_id = Column(Integer)

    def __init__(self, **kwargs):
        super(Books, self).__init__(**kwargs)


class testRecord(Base):
    __tablename__ = 'test_records'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, index=True, nullable=False)
    examid = Column(Integer, index=True, nullable=False)
    answer = Column(JSON)
    correct_info = Column(JSON)
    check = Column(Boolean, default=False)
    submit_time = Column(DateTime, nullable=False,
                         default=datetime.utcnow)
    modify_time = Column(DateTime, nullable=False,
                         default=datetime.utcnow)

    def __init__(self, **kwargs):
        super(testRecord, self).__init__(**kwargs)


class Exams(Base):
    __tablename__ = 'exams'
    id = Column(Integer, primary_key=True)
    text = Column(JSON)

    def __init__(self, **kwargs):
        super(Exams, self).__init__(**kwargs)
# admin = Users(username='admin', email='codeboycb@gmail.com', phone='13372364686', pswd='111', classid=1,
#               birthday=datetime.date(2006, 9, 11))
# 创建表
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# # 创建 Session 类实例
# session = Session()
#
# # 新增
# user = Users(username='admin',
#              email='codeboycb@gmail.com',
#              phone='13372364686',
#              pswd=generate_password_hash('20060911gyj'),
#              classid=1,
#              birthday=date(2006, 9, 11)
#              )
# # 保存
# session.add(user)
# # 提交
# session.commit()
# # 关闭
# session.close()
