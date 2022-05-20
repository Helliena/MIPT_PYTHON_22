import flask
import requests
import argparse
import cat
import time


host = 'localhost'
port = 5000

app = flask.Flask("cat")
app.cat = cat.Cat()


@app.route('/', methods=['GET'])
def greeting():
    return flask.render_template('page.html', chr=app.cat.watch())

@app.route('/feed', methods=['POST'])
def feed():
    app.cat.eat()
    app.cat.update()
    return flask.redirect('/')

@app.route('/drink', methods=['POST'])
def drink():
    app.cat.drink()
    app.cat.update()
    return flask.redirect('/')

@app.route('/chill', methods=['POST'])
def chill():
    app.cat.go_chill()
    app.cat.update()
    return flask.redirect('/')

@app.route('/sport', methods=['POST'])
def sport():
    app.cat.do_sport()
    app.cat.update()
    return flask.redirect('/')

if __name__ == '__main__':
    app.run(host, port)