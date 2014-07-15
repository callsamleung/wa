#coding:utf-8

import unittest
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.orm import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:keen@localhost/logsss'
db = SQLAlchemy(app)

class M_Logsss(db.Model):
    __tablename__ = 'logsss'
    id = Column(Integer, primary_key = True)
    id_code = Column(String(50), nullable = False)
    update_at = Column(DateTime(), nullable = False)
    create_at = Column(DateTime(), nullable = False)
    tags = Column(String(100), nullable = True)
    status = Column(Integer, nullable = False)
    content = Column(Text)
