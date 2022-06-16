# coding: utf-8
from sqlalchemy import Column, Integer, Numeric, String, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PosRaw(Base):
    __tablename__ = 'pos_raw'

    id = Column(Integer, primary_key=True)
    rid = Column(Integer)
    seq = Column(Integer)
    str = Column(String(255))
    pos = Column(String(255))


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    v_productcd = Column(String(255))
    v_productnm = Column(String(255))
    v_categorycd = Column(String(255))
    v_brandcd = Column(String(255))
    v_brandnm = Column(String(255))
    n_list_price = Column(Integer)
    n_price = Column(Integer)
    v_prod_ctg_path = Column(String(255))
    v_reg_dtm = Column(Numeric)
    json = Column(Text)


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    v_productcd = Column(String(255))
    v_optionnm = Column(String(255))
    n_recom_point = Column(Integer)
    v_content = Column(Text)
    n_content_len = Column(Integer)
    v_levelnm = Column(String(255))
    v_reg_dtm = Column(Numeric)
    json = Column(Text)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)
