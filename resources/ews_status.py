from flask_restful import Resource
import urllib2
import re
import json

class EWSStatus(Resource):
    def get(self):
        response = urllib2.urlopen("https://my.engr.illinois.edu/labtrack/util_data_json.asp")
        return json.load(response)
