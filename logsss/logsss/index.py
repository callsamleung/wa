#coding:utf-8

from datetime import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from view_logsss import content_status, Logsss, Content_tags
from model_logsss import M_Logsss
from lgs_content.lgs_index import lgs_index

app = Flask(__name__)
app.register_blueprint(lgs_index)
content_tags = Content_tags()
v_logsss = Logsss()
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        content_items = v_logsss.get_recorders()[:5]
        tags = content_tags.get_all()
        return render_template('index.html', content_items = content_items, tags = tags)
    if request.method == 'POST':
        status = request.form['status']
        tags = content_tags.trans_tags(request.form['content_tags'].split(','))
        new_obj = M_Logsss(id_code = 'adfjkwqeflwqelfjl', update_at = datetime.now(),\
                                   create_at = datetime.now(),\
                                   tags = ','.join(tags),\
                                   status = status,\
                                   content = request.form['content'])
        if v_logsss.add_logsss(new_obj):
            return redirect(url_for('index'))
        else:
            return 'commit error'
    return 'nothing here'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
