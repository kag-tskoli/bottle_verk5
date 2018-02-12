from bottle import route, run, template
import os
import requests
#import json

response = requests.get('http://apis.is/concerts')

data = response.json()


@route('/')
def index():
    return template('index', data=data)


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
