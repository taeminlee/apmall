#%%
import sqlite3

def main():
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    with open('input.txt', 'w', encoding='utf-8') as f:
        for rrow in conn.cursor().execute("""select review.id, v_categorycd from review join product on (review.v_productcd = product.v_productcd) 
            where v_brandnm = '마몽드'"""):
            curs.execute("""select str from pos_raw where rid = %s""" % rrow[0])
            strs = list(map(lambda row:row[0], curs.fetchall()))
            if(len(strs) == 0):
                continue
            line = "%s %s\n" % (rrow[0], " ".join(strs))
            f.write(line)
main()