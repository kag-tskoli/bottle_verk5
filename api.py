from bottle import route, run, template
import requests
#import json

response = requests.get('http://apis.is/concerts')

data = response.json()


@route('/')
def index():
    return template('index', data=data)


run()