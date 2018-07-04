# -*- coding: utf-8 -*-
#%% impot libraries
import sqlite3
import requests
import pickle
import json
import sys
import os
from konlpy.tag import Kkma, Twitter
#from twkorean import TwitterKoreanProcessor

kkma = Kkma()
twitter = Twitter()
#processor = TwitterKoreanProcessor(stemming=False)

buffer = []

def pos_list(content):
    #return kkma.morphs(content, flatten=False)
    return twitter.morphs(content)
    #return processor.tokenize(content)

#%% functions
def sqlite3_conn():
    return sqlite3.connect('data.db')

def create_db():
    conn = sqlite3_conn()
    curs = conn.cursor()
    pos_raw_sql = """CREATE TABLE IF NOT EXISTS pos_raw (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rid int,
        seq int,
        str varchar(255),
        pos varchar(255)
        );"""
    curs.execute(pos_raw_sql)
    conn.commit()

def truncate_table(curs, table_name):
    sql = "delete from %s" % table_name
    curs.execute(sql)
    

def review_pos_raw_gen(curs):
    sql = "select * from review"
    for row in curs.execute(sql):
        seq = 0
        rid = row[0]
        if len(row[4]) < 120:
            continue
        if row[4] in buffer:
            continue
        buffer.append(row[4])
        try:
            #print('before pos_list')
            poss = pos_list(row[4])
            print(poss)
            #print('after pos_list')
            print(rid)
            for pos in poss:
                #print(pos)
                args = (rid, seq, pos, None)
                yield args
                seq = seq+1
        except Exception:
            print(row)

def insert_pos_raw(curs, args):
    sql = "insert into pos_raw values(null, %s)" % (", ".join(["?"] * len(args)))
    curs.execute(sql, args)

def run_pos_raw():
    create_db()
    conn = sqlite3_conn()
    select_curs = conn.cursor()
    insert_curs = conn.cursor()
    truncate_table(select_curs, "pos_raw")
    cnt = 0
    for pos_raw_args in review_pos_raw_gen(select_curs):
        cnt = cnt+1
        if cnt % 100 == 0:
            #print(cnt)
            conn.commit()
        insert_pos_raw(insert_curs, pos_raw_args)
    #print(cnt)
    conn.commit()

if __name__ == '__main__':
    try:
        run_pos_raw()
    except KeyboardInterrupt:
        print("Exit")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)