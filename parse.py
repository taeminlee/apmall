# -*- coding: utf-8 -*-
#%% impot libraries
import sqlite3
import requests
import pickle
import json
import sys
import os
from konlpy.tag import Kkma

#%% kkma test
kkma = Kkma()
def kkma_test(test_str = None):
    if test_str is None:
        test_str = "users_s 표절검사 대상 사용자 집합을 정의한다. withcs 시스템의 경우 공개형 강의 플랫폼으로 외부인 역시 참여 가능하다. 과제의 평가 관점에서 수강생에 대해서만 상호 표절 검사를 진행해야 한다."
    #print(test_str)
    return kkma.pos(test_str, flatten=True)

print(kkma_test())

def pos_list(content):
    return kkma.pos(content, flatten=True)

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
    sql = "truncate %s" % table_name
    curs.execute(sql)
    

def review_pos_raw_gen(curs):
    sql = "select * from review"
    for row in curs.execute(sql):
        rid = row[0]
        seq = 0
        poss = pos_list(row[4])
        print(poss)
        for pos in poss:
            args = (rid, seq, pos[0], pos[1])
            yield args
            seq = seq+1

def insert_pos_raw(curs, args):
    sql = "insert into pos_raw values(null, %s)" % (", ".join(["?"] * len(args)))
    curs.execute(sql, args)

def run_pos_raw():
    create_db()
    truncate_table("pos_raw")
    conn = sqlite3_conn()
    select_curs = conn.cursor()
    insert_curs = conn.cursor()
    cnt = 0
    for pos_raw_args in review_pos_raw_gen(select_curs):
        cnt = cnt+1
        if cnt % 100 == 0:
            print(cnt/100)
            conn.commit()
        insert_pos_raw(insert_curs, pos_raw_args)
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