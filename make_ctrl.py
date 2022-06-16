# ctrl 학습 용으로 데이터 가공

# 데이터 가공

# CATEGORY_CODE SCORE_CODE PRODUCT_NAME DESC

# CATEGORY_CODE = 'CAT'+CATEGORY_NAME (single token)
# SCORE_CODE = 'SCORE'+SCORE (single token)
# PRODUCT_NAME = PRODUCT_NAME (multi token)
# DESC = DESC (multi token)

# DialoGPT 학습 코드로 학습

# 1.0 CATEGORY_CODE SCORE_CODE PRODUCT_NAME EOS DESC[0] EOS DESC[1] ... \t 1.0 DESC[-1]

# python
import json

# 3rd-party
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import tqdm
import kss

# framework
import model

def code_to_token(codes, code):
    idx = codes.index(code)
    return "<unused{0}>".format(idx)
def encode_category(val, p=None):
    return 'CAT'+val.split('>')[0].replace(' ','')
def encode_score(val):
    return 'SCORE'+str(val)
def make_dialogue(text):
    text = text.replace('\r\n', '')
    text = text.replace('\n', '')
    sents = kss.split_sentences(text)
    return sents
    return ' EOS '.join(sents[:-1]) + '\t' + sents[-1]

if __name__ == "__main__":
    engine = sa.create_engine('sqlite:///data.db')
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    tsv_f = open('apmall.tsv', 'w', encoding='utf-8')
    eval_f = open('eval.tsv', 'w', encoding='utf-8')

    codes = {}

    P = session.query(model.Product).all()
    for p in tqdm.tqdm(P):
        R = session.query(model.Review).filter(model.Review.v_productcd == p.v_productcd).all()
        for r in tqdm.tqdm(R):

            # print(p.__dict__)
            # print(r.__dict__)

            if(p.v_categorycd == ''):
                # 카테고리 코드가 없는 제품의 경우 무시하고 넘어감
                continue

            cat_code = encode_category(p.v_prod_ctg_path, p)
            score_code = encode_score(r.n_recom_point)

            if(cat_code not in codes.keys()):
                codes[cat_code] = "<unused{0}>".format(len(codes))
            if(score_code not in codes.keys()):
                codes[score_code] = "<unused{0}>".format(len(codes))

            header = [' '.join(['1.0', codes[cat_code], codes[score_code], p.v_productnm])]
            body = make_dialogue(r.v_content)
            sents = header + body
            line = ' EOS '.join(sents[:-1]) + '\t 1.0 ' + sents[-1]

            print(line, file=tsv_f)

            header = [' '.join([codes[cat_code], codes[score_code], p.v_productnm])]
            body = make_dialogue(r.v_content)
            sents = header + body
            for i in range(len(sents)-1):
                print('\t'.join(sents[i:i+2]), file=eval_f)
    
    with open('codes.json', 'w') as fp:
        json.dump(codes, fp, ensure_ascii=False)
    
    print('done')