# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine(
    'mysql+pymysql://root:root@127.0.0.1:3306/test',
    echo=True
)

class Book(Base):

    __tablename__ = 'book'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(64))
    info = Column(String(64))
    intro = Column(Text())
    rating_num = Column(String(16))
    rating_people = Column(String(16))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sess = Session()