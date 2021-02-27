# -*- encoding: utf-8 -*-
"""
@File    :   config.py    
@Contact :   codeboycb@gmail.com
@License :   (C)Copyright 2020-present,Guan Yongjie 官咏颉 
"""

# 配置数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:20060911@localhost:3306/ris'
# 设置每次请求结束后会自动提交数据库的改动
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 查询时显示原始SQL语句
SQLALCHEMY_ECHO = True

