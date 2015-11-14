from flask_restful import Resource
import urllib2
import json

class Dining(Resource):
    def get(self):
      request_url = "http://23.23.147.128/homes/mydata/urba7723"
      response = urllib2.urlopen(request_url)
      return json.load(response)
