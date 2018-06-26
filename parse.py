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

#%% functions
def sqlite3_conn():
    return sqlite3.connect('data.db')

def create_db():
    conn = sqlite3_conn()
    curs = conn.cursor()
    review_sql = """CREATE TABLE IF NOT EXISTS review (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        v_productcd varchar(255),
        v_optionnm varchar(255),
        n_recom_point INT,
        v_content TEXT,
        n_content_len INT,
        v_levelnm varchar(255),
        v_reg_dtm LONG,
        json TEXT
        );"""
    curs.execute(review_sql)
    product_sql = """CREATE TABLE IF NOT EXISTS product (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        v_productcd varchar(255),
        v_productnm varchar(255),
        v_categorycd varchar(255),
        v_brandcd varchar(255),
        v_brandnm varchar(255),
        n_list_price INT,
        n_price INT,
        v_prod_ctg_path varchar(255),
        v_reg_dtm LONG,
        json TEXT
        );"""
    curs.execute(product_sql)
    conn.commit()