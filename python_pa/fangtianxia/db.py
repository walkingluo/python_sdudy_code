# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine(
    'mysql+pymysql://root:root@127.0.0.1:3306/test',
    max_overflow=5,
    pool_size=10,
    echo=True
)

class Fang(Base):

    __tablename__ = 'fang'

    id = Column('ID', Integer, primary_key=True)
    title = Column('标题', String(64))
    unit_type = Column('户型', String(64))
    area = Column('面积', String(64))
    price = Column('单价', String(64))
    year = Column('年代', String(64))
    sale_point = Column('卖点', Text())


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sess = scoped_session(Session)