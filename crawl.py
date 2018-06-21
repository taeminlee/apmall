# -*- coding: utf-8 -*-
#%% impot libraries
import sqlite3
import requests
import pickle
import json
import sys
import os

def sqlite3_conn():
    return sqlite3.connect('data.db')

def create_db():
    conn = sqlite3_conn()
    curs = conn.cursor()
    review_sql = """CREATE TABLE IF NOT EXISTS review (
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

def product_gen(category=None,brand=None):
    global product_cache
    url = "http://www.amorepacificmall.com/mobile/shop/mobile_shop_category_product_list_ajax.do"
    max_page = 1000
    page = 1
    while page <= max_page:
        data = {
            'i_iNowPageNo' : page
        }
        page = page + 1
        if category is not None:
            data['i_sCategorycd1'] = category
        if brand is not None:
            data['i_sBrandcd'] = brand
        datastr = json.dumps(data)
        if(datastr in product_cache):
            max_page = int(product_cache[datastr]['object']['shopprd']['page']['i_iTotalPageCnt'])
            yield product_cache[datastr]['object']['shopprd']['list']
        else:
            res = requests.post(url = url, data = data)
            result = res.json()
            product_cache[datastr] = result
            max_page = int(result['object']['shopprd']['page']['i_iTotalPageCnt'])

            yield result['object']['shopprd']['list']

def review_gen(productId):
    global review_cache
    url = "http://www.amorepacificmall.com/mobile/shop/mobile_shop_product_review_ajax.do"
    max_page = 1000
    page = 1
    while page <= max_page:
        data = {
            'i_iNowPageNo' : page,
            'i_sTypecd' : '0004',
            'i_sProductcd' : productId
        }
        page = page + 1
        datastr = json.dumps(data)
        if(datastr in review_cache):
            max_page = int(review_cache[datastr]['object']['textReview']['page']['i_iTotalPageCnt'])
            yield review_cache[datastr]['object']['textReview']['list']
        else:
            res = requests.post(url = url, data = data)
            result = res.json()
            review_cache[datastr] = result
            max_page = int(result['object']['textReview']['page']['i_iTotalPageCnt'])

            yield result['object']['textReview']['list']

def process_product_list(curs, product_list):
    for item in product_list:
        try:
            args = []
            args.append(item['v_productcd'])
            args.append(item['v_productnm'])
            if 'v_categorycd' in item:
                args.append(item['v_categorycd'])
            else:
                args.append("")
            args.append(item['v_brandcd'])
            args.append(item['v_brandnm'])
            args.append(int(item['n_list_price']))
            args.append(int(item['n_price']))
            if 'v_prod_ctg_path' in item:
                args.append(item['v_prod_ctg_path'])
            else:
                args.append('')
            args.append(int(item['v_reg_dtm']))
            args.append(json.dumps(item, ensure_ascii=False))
            sql = "insert into product values (%s)" % (", ".join(["?"] * len(args)))
            #print(sql)
            curs.execute(sql, args)
        except Exception as e:
            print(str(e))
            print(item)

def process_review_list(curs, review_list):
    for item in review_list:
        try:
            args = []
            args.append(item['v_productcd'])
            if "v_optionnm" in item:
                args.append(item['v_optionnm'])
            else:
                args.append("")
            args.append(int(item['n_recom_point']))
            args.append(item['v_content'])
            args.append(len(item['v_content']))
            args.append(item['v_levelnm'])
            args.append(int(item['v_reg_dtm']))
            args.append(json.dumps(item, ensure_ascii=False))
            sql = "insert into review values (%s)" % (", ".join(["?"] * len(args)))
            #print(sql)
            curs.execute(sql, args)
        except Exception as e:
            print(str(e))
            print(item)

def init_cache():
    global product_cache, review_cache
    try:
        with open('product.cache', 'rb') as f:
            product_cache = pickle.load(f)
        with open('review.cache', 'rb') as f:
            review_cache = pickle.load(f)
        print("load cache")
    except:
        product_cache = {}
        review_cache = {}
        print("init cache")
   
def run_all():
    global product_cache, review_cache
    init_cache()
    try:
        create_db()
        conn = sqlite3_conn()
        curs = conn.cursor()
        curs.execute("delete from product")
        conn.commit()
        for product_list in product_gen():
            print(product_list[0]['v_productnm'], len(product_list))
            process_product_list(curs, product_list)
            conn.commit()
        curs.execute("delete from review")
        conn.commit()
        curs.execute("select distinct(v_productcd) from product")
        productIds = list(map(lambda row: row[0], curs.fetchall()))
        pageNum = 0
        for productId in productIds:
            print(pageNum, len(productIds))
            pageNum = pageNum + 1
            for review_list in review_gen(productId):
                print(review_list[0]['v_content'], len(review_list))
                process_review_list(curs, review_list)
                conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        with open('product.cache', 'wb') as f:
            pickle.dump(product_cache, f)
        with open('review.cache', 'wb') as f:
            pickle.dump(review_cache, f)

product_cache = {}
review_cache = {}

if __name__ == '__main__':
    try:
        run_all()
    except KeyboardInterrupt:
        print("Exit")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)