# -*- coding: utf-8 -*-
#%% impot libraries
import sqlite3
import pickle
import io

#%% functions
def sqlite3_conn():
    return sqlite3.connect('data.db')

def create_db(pos_raw_sql):
    conn = sqlite3_conn()
    curs = conn.cursor()
    curs.execute(pos_raw_sql)
    conn.commit()

def truncate_table(curs, table_name):
    sql = "delete from %s" % table_name
    curs.execute(sql)

def load_dic():
    try:
        return pickle.load(io.open('dic.pkl', 'rb'))
    except:
        print("please execute python makedic.py")
        return []