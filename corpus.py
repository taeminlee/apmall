#%%
import sqlite3

def main():
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    with open('train.txt', 'w'):
        for row in curs.execute("""
            select * from pos_raw join review on (pos_raw.rid = review.id) join product on (review.v_productcd = product.v_productcd) 
            where v_brandnm = '아이오페'
            """):
            print(dir(row))
            input()

main()