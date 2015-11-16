from flask_restful import Resource
import urllib2
import json

class FreeFood(Resource):
    def get(self):
        response = urllib2.urlopen("http://uiucfreefood.com/appJson/")
        return json.load(response)
