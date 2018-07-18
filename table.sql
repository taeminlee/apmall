CREATE TABLE IF NOT EXISTS pos_raw (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rid int,
    seq int,
    str varchar(255),
    pos varchar(255)
);

CREATE TABLE IF NOT EXISTS review (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    v_productcd varchar(255),
    v_optionnm varchar(255),
    n_recom_point INT,
    v_content TEXT,
    n_content_len INT,
    v_levelnm varchar(255),
    v_reg_dtm LONG,
    json TEXT
); 

CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
)