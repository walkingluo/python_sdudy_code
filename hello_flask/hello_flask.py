# -*- coding:utf-8 -*-

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/hello/<name>/')
def hello(name):
    return flask.render_template('hello.html', name=name)


if __name__ == '__main__':
    app.debug = True
    app.run()