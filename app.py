#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
from flask import Flask,request
from base.base import *
app = Flask(__name__)

@app.before_request
def before_request():
    if request.method == 'POST' and request.form.get("name"):
        name=request.form.get("name")
        if existfile(name):
            if ran(5):
                return readcache(name)
    elif request.args.get("name"):
        name = request.args.get("name")
        if existfile(name):
            if ran(5):#概率5-->5%的概率更新缓存
                return readcache(name),{"Content-Type":"application/json","server":"qq","time":"Hello"}


@app.after_request
def after_request(environ):
    if True:#文件缓存
        data=environ.data.decode('UTF-8')
        if request.method == 'POST' and request.form.get("name"):
            name=request.form.get("name")
            writecache(name,data)
        elif request.args.get("name"):
            name = request.args.get("name")
            writecache(name,data)
    return  environ


@app.route('/')
def hello_world():
    return '调用方式/api?name=视频名称[GET|POST] return JSON'

@app.route('/api',methods=['GET','POST'])
def api():
    if request.method=='POST':
        name=request.form.get("name")
        data=json.dumps(run(name))
        return data
    else:
        name = request.args.get("name")
        data=run(name)
        jsondata = json.dumps(data)
        return jsondata,{"Content-Type":"application/json","server":"qq"}


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,threaded=True,debug=True)
    #app.run(host='0.0.0.0', port=8081, threaded=True, debug=False)