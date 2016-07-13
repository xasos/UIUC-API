from flask_restful import Resource
import urllib2, json, os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../tools/professors.json')

class FacultyDirectory(Resource):
    def get(self):
      with open(filename, 'r') as data_file:
          return json.load(data_file)
