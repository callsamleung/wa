#coding:utf-8

import unittest
from model_logsss import M_Logsss, db
from datetime import datetime

class Content_tags():
    CONTENT_TAGS = {1:'emacs',\
                        2:'test',\
                        }
    def __init__(self):
        pass
    def trans_tags(self, tag_indexes):
        tag_indexes = tuple(tag_indexes)
        return [self.CONTENT_TAGS.get(int(t)) for t in tag_indexes]
    def get_tag(self, index):
        return self.CONTENT_TAGS.get(index)
    def get_all_tags(self):
        return self.CONTENT_TAGS.values()
    def get_all(self):
        return self.CONTENT_TAGS
    def validate_value(self, tags_value):
        return tags_value in self.CONTENT_TAGS.values()

class Test_Content_tags(unittest.TestCase):
    def setUp(self):
        self.t = Content_tags()
    def test_trans_tags(self):
        tags_index = '1'.split(',')
        result = [self.t.CONTENT_TAGS.get(int(i)) for i in tags_index]
        test_result = self.t.trans_tags(tags_index)
        self.assertEqual(tuple(result), tuple(test_result))
        tags_index = '1,2'.split(',')
        result = [self.t.CONTENT_TAGS.get(int(i)) for i in tags_index]
        test_result = self.t.trans_tags(tags_index)
        self.assertEqual(tuple(result), tuple(test_result))
    def test_validate_value(self):
        tags = 'test'
        true_result = self.t.validate_value(tags)
        self.assertTrue(true_result)
        tags = 'must no exists result'
        false_result = self.t.validate_value(tags)
        self.assertFalse(false_result)
    def test_get_tag(self):
        tags_index = 1
        result = self.t.CONTENT_TAGS.get(tags_index)
        test_result = self.t.get_tag(tags_index)
        self.assertEqual(result, test_result)
    def test_get_all_tags(self):
        result = tuple(self.t.CONTENT_TAGS.values())
        test_result = tuple(self.t.get_all_tags())
        self.assertEqual(result, test_result)
    def test_get_all(self):
        result = self.t.CONTENT_TAGS
        test_result = self.t.get_all()
        self.assertEqual(result, test_result)

class Content_status():
    def __init__(self):
        self.draft = 0
        self.publish = 1

class Test_Content_status(unittest.TestCase):
    def setUp(self):
        self.c = Content_status()
    def test_status(self):
        self.assertTrue(self.c.draft == 0)
        self.assertTrue(self.c.publish == 1)

content_status = Content_status()

class Logsss():
    '''
    quick_view:
        get_draft
        get_item
        get_recorders
        add_logsss
        get_recorders_with
    '''
    def __init__(self):
        pass
    def get_draft(self, identity):
        identity = int(identity)
        recorder = db.session.query(M_Logsss).filter_by(id = identity, status = content_status).first()
        return recorder
    def get_item(self, identity):
        identity = int(identity)
        recorder = db.session.query(M_Logsss).filter_by(id = identity).first()
        return recorder
    def get_recorders(self):
        return db.session.query(M_Logsss).order_by("id desc")
    def get_recorders_with(self, tags):
        return db.session.query(M_Logsss).filter(M_Logsss.tags.like(tags)).order_by('id desc')
    def add_logsss(self,logsss_model):
        is_success = False
        try:
            db.session.add(logsss_model)
            db.session.commit()
            is_success = True
        except:
            is_success = False
        return is_success

            

class Test_Logsss(unittest.TestCase):
    def setUp(self):
        self.l = Logsss()
    def test_add_logsss(self):
        new_obj = M_Logsss(id_code = 'adfjkwqeflwqelfjl', update_at = datetime.now(),\
                               create_at = datetime.now(),\
                               tags = 'test',\
                               status = content_status.draft,\
                               content = 'content_test')
        result = self.l.add_logsss(new_obj)
        self.assertTrue(result)
    def test_get_draft(self):
        ids = '0'
        obj = self.l.get_draft(ids)
        self.assertFalse(obj) # test exists
        #test content
        new_obj = M_Logsss(id_code = 'adfjkwqeflwqelfjl', update_at = datetime.now(),\
                               create_at = datetime.now(),\
                               tags = 'test',\
                               status = content_status.draft,\
                               content = 'content_test')
        db.session.add(new_obj)
        db.session.commit()
        ids = new_obj.id
        obj = self.l.get_draft(ids)
        self.assertEqual('content_test', obj.content)
    def test_get_logsss(self):
        ids = 0
        obj = self.l.get_item(ids)
        self.assertTrue(obj == None) # test exists
    def test_get_recorders(self):
        r = self.l.get_recorders()
        r = r.all()
        self.assertTrue(len(r) > 0)
    def test_get_recorders_with(self):
        tags = 'test,emacs'
        new_obj = M_Logsss(id_code = 'adfjkwqeflwqelfjl', update_at = datetime.now(),\
                               create_at = datetime.now(),\
                               tags = tags,\
                               status = content_status.draft,\
                               content = 'content_test')
        db.session.add(new_obj)
        db.session.commit()
        identity = new_obj.id
        result = [o.id for o in self.l.get_recorders_with(tags)]
        self.assertTrue(identity in result)
        

if __name__ == '__main__':
    unittest.main()
