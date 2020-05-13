# -*- conding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table

# 参数字符串说明：数据库类型+驱动://用户名:密码@主机:端口号/数据库名字?charset=编码格式
# mysql 自带驱动，密码未设定，端口号可省略
engine = create_engine('mysql://root:password@localhost/study?charset=utf8')
# 创建映射类需要继承声明基类
# 创建声明基类时传入引擎
Base = declarative_base(engine)


class User(Base):
    """docstring for User"""
    __tablename__ = 'user'    # 设置数据表名字，不可省略

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    email = Column(String(64), unique=True)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


class Course(Base):
    """docstring for Course"""
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    # ForeignKey 设置外键关联，第一个参数为字符串，user 为数据表名，id 为字段名
    # 第二个参数 ondelete 设置删除 User 实例后对关联的 Course 实例的处理规则
    # 'CASCADE' 表示级联删除，删除用户实例后，对应的课程实例也会被连带删除
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    # relationship 设置查询接口，以便后期进行数据库查询操作
    # 第一个参数为位置参数，参数值为外键关联的映射类名，数据类型为字符串
    # 第二个参数 backref 设置反向查询接口
    # backref 的第一个参数 'course' 为查询属性，User 实例使用该属性可以获得相关课程实例的列表
    # backref 的第二个参数 cascade 如此设置即可实现 Python 语句删除用户数据时级联删除课程数据
    user = relationship('User', backref=backref('course', cascade='all, delete-orphan'))

    def __repr__(self):
        return '<Course: {}>'.format(self.name)


class Lab(Base):
    """docstring for Lab"""
    __tablename__ = 'lab'

    id = Column(Integer, ForeignKey('course.id'), primary_key=True)
    name = Column(String(128))
    course = relationship('Course', backref=backref('lab', uselist=False))

    def __repr__(self):
        return '<Lab: {}>'.format(self.name)


Rela = Table('rela', Base.metadata,
        Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('course.id'), primary_key=True))


class Tag(Base):
    """docstring for Tag"""
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    course = relationship('Course', secondary=Rela, backref='tag')

    def __repr__(self):
        return '<Tag: {}>'.format(self.name)


if __name__ == '__main__':

    Base.metadata.create_all()




