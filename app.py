 # -*- coding: UTF-8 -*-

from flask import Flask

def creat_app():
    app = Flask(__name__)
    return  app

app = creat_app()

@app.route('/')
def index():
    return "hello world！"

if __name__ == '__main__':
    app.run()
