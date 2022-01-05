# -*- coding:utf-8 -*-

from sqlalchemy import create_engine, Table
from sqlalchemy import Column, Integer, String, select, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 表基类
Base = declarative_base()

engine = create_engine(
    'mysql+pymysql://root:root@127.0.0.1:3306/test',
    max_overflow=5,
    pool_size=10,
    echo=True
)

# metadata = MetaData()

""" user = Table('user', metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('name', String(20))
            ) """

# 通过元数据创建表
#metadata.create_all(engine)

# 直接执行sql语句，进行增删改查
# engine.execute("insert into user (name) values ('apple');")
""" res = engine.execute("select * from user;")
for r in res:
    print(r) """

# 使用表结构进行增删改查
# conn = engine.connect()
# conn.execute(user.insert(), {'name': 'python'})
# conn.execute(user.update().where(user.c.id==2).values(name='c++'))
# res = conn.execute(select([user.c.id, user.c.name]))
# print(res.fetchall())
# conn.execute(user.delete().where(user.c.id==2))
# conn.close()

# ORM
class Host(Base):
    # 表名
    __tablename__ = 'hosts'
    # 表结构
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=2333)

user2lang = Table('user_2_lang', Base.metadata,
                    Column('user_id', ForeignKey('user.id'), primary_key=True),
                    Column('lang_id', ForeignKey('language.id'), primary_key=True))

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=True)
    gender = Column(String(10), nullable=True, default='unknow')
    town = Column(String(128))
    language = relationship('Language', secondary=user2lang, backref='user', cascade='all, delete')

class Language(Base):

    __tablename__ = 'language'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=True)
    advantage = Column(String(128), nullable=True)
    disadvantage = Column(String(128), nullable=True)
    # user_id = Column(Integer(), ForeignKey('user.id'))

def create_table():

    # 创建表
    Base.metadata.create_all(engine)

def execute_table():

    Session = sessionmaker(bind=engine)
    sess = Session()  # 创建实例
    '''
    h1 = Host(hostname='test1', ip_addr='127.0.0.1')
    h2 = Host(hostname='test2', ip_addr='192.168.1.100', port=1000)
    h3 = Host(hostname='test3', ip_addr='192.168.1.101', port=1001)

    # sess.add(h1)
    # sess.add_all([h2,h3])
    # sess.query(Host).filter(Host.id>2).delete()
    # sess.query(Host).filter(Host.id==2).update({'port': 8888})
    res = sess.query(Host).filter_by(id=1).all()
    for r in res:
        print(r.hostname, r.port)
    sess.commit() 
    '''
    '''
    u1 = User(name="张三", gender="男", town="北京")
    u2 = User(name="李四", gender="男", town="广州")
    sess.add_all([u1, u2])
    sess.commit()

    l1 = Language(name="python", advantage="开发快", disadvantage="运行慢")
    l1.user = u1
    sess.add(l1)
    sess.commit()
    '''
    u3 = User(name="王五", gender="女", town="上海")
    u3.language = [Language(
                        name="C++", 
                        advantage="运行快", 
                        disadvantage="上手慢"),
                   Language(
                       name="go", 
                       advantage="运行快", 
                       disadvantage="更易上手")]
    sess.add(u3)
    sess.commit()
    '''
    u = sess.query(User).filter_by(id=3).first()
    print("name: ", u.name)
    lang = sess.query(Language).filter_by(id=u.id).all()
    for l in lang:
        print("language: ", l.name)
    sess.commit()
    '''
    '''
    # 如有外键会报错
    #sess.query(Language).filter_by(user_id=4).delete()
    sess.query(User).filter_by(id=3).delete()
    sess.commit()
    
    # 没有设置cascade，可删除，但外键会变为NULL
    u = sess.query(User).filter_by(id=4).first()
    # sess.delete(u)
    u.name = '赵六'
    sess.commit()
    '''

if __name__ == '__main__':
    
    # create_table()
    execute_table()
