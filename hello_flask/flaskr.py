# 导入所有的模块
import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# 配置文件
DATABASE = './flaskr.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read().decode())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')   # 查询语句
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]   # 将查询结果转换为字典
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',[request.form['title'], request.form['text']])   # 向数据库中插入数据
    g.db.commit()   # 更新数据
    flash('New entry was successfully posted')   # 闪现一条消息
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:   # 如果用户名不符合
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:   # 如果密码不符合
            error = 'Invalid password'
        else:
            session['logged_in'] = True   # 成功登录，在 session 中添加一个 logged_in 值为 True
            flash('You were logged in')   # 闪现一条消息
            return redirect(url_for('show_entries'))   # 重定向到首页
    return render_template('login_f.html', error=error)   # 如果没有成功登录则返回登录页面以及错误信息

@app.route('/logout')
def logout():
    session.pop('logged_in', None)   # 移除 logged_in 键
    flash('You were logged out')   # 闪现消息
    return redirect(url_for('show_entries'))   # 重定向到首页

if __name__ == '__main__':
    app.run()