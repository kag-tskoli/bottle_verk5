from bottle import route, run, template, static_file
import os
import requests
#import json

response = requests.get('http://apis.is/concerts')

data = response.json()


@route('/')
def index():
    return template('index', data=data)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
