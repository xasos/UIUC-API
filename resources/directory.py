from flask_restful import Resource
import urllib2
import re

class Directory(Resource):
    def get(self, query, search_type):  # construct URL
      request_url = "https://illinois.edu/ds/search?skinId=0&sub=&search=niraj+pant&search_type=all";
      response = urllib2.urlopen(request_url)


