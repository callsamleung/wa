#coding:utf-8

from model_logsss import db

if __name__ == '__main__':
    try:
        db.create_all()
        print 'db.create_all OK'
    except Exception, e:
        print e
