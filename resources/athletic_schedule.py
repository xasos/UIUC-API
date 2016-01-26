from flask_restful import Resource
import urllib2
import xml2json

BASE_URL = ""
sports = ['wcross', 'wcross', 'wsoc', 'mbball',
'wbball', 'wswim', 'mgym', 'wgym', 'wrestling',
'baseball', 'softball', 'mgolf', 'wgolf', 'mtrack',
'wtrack', 'mten', 'wten']

class AthleticSchedule(Resource):
    def get(self, sport):
        if sport.lower() in sports:
            request_url = BASE_URL + sport + END_URL
            request = urllib2.urlopen(request_url)
            return xml2json(request)
        else:
            return ""
