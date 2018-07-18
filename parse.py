# -*- coding: utf-8 -*-
#%% impot libraries
import requests
import pickle
import json
import sys
import os
from konlpy.tag import Kkma, Twitter
import util
from functools import reduce
#from twkorean import TwitterKoreanProcessor

kkma = Kkma()
twitter = Twitter()
#processor = TwitterKoreanProcessor(stemming=False)

buffer = []

dic = util.load_dic()

def pos_list(content):
    #return kkma.morphs(content, flatten=False)
    morphs = twitter.morphs(content)
    # 사전의 단어가 존재하면 분절화된 경우 다시 합침
    for token in dic:
        if token in content:
            if token not in morphs:
                print(token)
                buffer = ""
                start_idx = -1
                end_idx = -1
                bias = 0
                merge_candidates = []
                for idx, morph in enumerate(morphs):
                    if token.startswith(morph):
                        buffer = morph
                        start_idx = idx
                    elif token.startswith(buffer + morph):
                        buffer = buffer + morph
                    else:
                        buffer = ""
                    if buffer == token:
                        end_idx = idx
                        buffer = ""
                        merge_candidates.append((start_idx - bias, end_idx - bias))
                        bias = bias + end_idx - start_idx
                if len(merge_candidates) > 0:
                    for merge_idx in merge_candidates:
                        morphs = morphs[0:merge_idx[0]] + [token] + morphs[merge_idx[1]+1:]
                        if(merge_idx[1]-merge_idx[0] > 1):
                            print(morphs)
                            print(merge_candidates)
                            input()
    return morphs

    #return processor.tokenize(content)    

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
            #print(poss)
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
    util.create_db("""CREATE TABLE IF NOT EXISTS pos_raw (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rid int,
        seq int,
        str varchar(255),
        pos varchar(255)
        );""")
    conn = util.sqlite3_conn()
    select_curs = conn.cursor()
    insert_curs = conn.cursor()
    util.truncate_table(select_curs, "pos_raw")
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
