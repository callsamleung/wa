##Introduction

build for reading Flask, sqlalchemy.

##HOW TO USE

BEFORE:

1. fix database setting at model_logsss.py

THEN:

1. git clone https://github.com/callsamleung/logsss
2. cd logsss
3. python db.init.py (your will see ok)
4. python index.py

##CHANGLOG

20140714:

1. test blueprint for url('/l') route


20140709:

1. list data @ index.html
2. add class Content_tags @ view_logsss.py


20140708:

1. data struct: content(text), id_code(string), status(int), update_at(datetime), create_at(datetime), tags(string)
