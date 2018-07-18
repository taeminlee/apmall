# -*- coding:utf-8 -*-
import util
import sys
import pickle
import io

def make_dic():
    conn = util.sqlite3_conn()
    curs = conn.cursor()
    sql = "select v_productnm, v_brandnm from product"
    tokens = []
    for row in  curs.execute(sql):
        for name in row:
            list(map(lambda token:append(tokens, token), name.split()))
    pickle.dump(tokens, io.open('dic.pkl', 'wb'))

def append(lst, elem):
    if len(elem) > 1 and elem not in lst:
        lst.append(elem)

if __name__ == '__main__':
    sys.exit(make_dic())