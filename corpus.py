#%%
import util
import sys

parser = argparse.ArgumentParser(description='Training corpus generator')
parser.add_argument('--mode', default='word-rnn', help='data target : word-rnn or GloVe')
args = parser.parse_args()

input_name = args.mode + ".txt"

if(args.mode == 'word-rnn'):
    input_name = 'input.txt'

def main():
    conn = util.sqlite3_conn()
    curs = conn.cursor()
    curs2 = conn.cursor()
    with open(input_name, 'w', encoding='utf-8') as f:
        for rrow in curs2.execute("""select review.id, v_categorycd, v_brandnm, v_productnm from review join product on (review.v_productcd = product.v_productcd) 
            """):
            curs.execute("""select str from pos_raw where rid = %s""" % rrow[0])
            strs = list(map(lambda row:row[0], curs.fetchall()))
            if(len(strs) == 0):
                continue
            if(args.mode == 'word-rnn'):
                line = "[-%s %s-] %s\n" % (rrow[3], rrow[2], " ".join(strs))
            else:
                line = "%s\n" % (" ".join(strs))
            print(rrow[0])
            f.write(line)

if __name__ == '__main__':
    sys.exit(create_corpus())
