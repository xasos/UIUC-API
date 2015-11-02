from flask import Flask
from flask_restful import Resource, Api
from bs4 import BeautifulSoup
from IPython import embed
import urllib2
import re

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
  def get(self):
    webpage = urllib2.urlopen("http://dailyillini.com/")
    soup = BeautifulSoup(webpage, "html.parser")
    embed()
    soup.find_all('article')

api.add_resource(HelloWorld, '/')

if __name__ == '__main__'
  app.run(debug=True)
