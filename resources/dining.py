from flask_restful import Resource, reqparse
import urllib2
import json
import requests

class Dining(Resource):
    def get(self):
        request_url = "https://web.housing.illinois.edu/MobileDining/WebService/Search.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04"
        # Add route parameters
        request_url += "?id=" + hallId + "&from=" + fromDate + "&to=" + toDate + "&t=json"
        response = urllib2.urlopen(request_url)
        return json.load(response)

    def post(self, username, password):
        request_url = "https://webservices.admin.uillinois.edu/aitsWS/security/login/json"
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': '39', 'User-Agent': 'UI%20Dining/15 CFNetwork/758.1.6 Darwin/15.0.0', 'Connection': 'keep-alive', 'Accept-Language': 'en-us', 'Accept-Encoding': 'gzip, deflate', 'Proxy-Connection': 'keep-alive', 'Host': 'webservices.admin.uillinois.edu'}
        req = requests.post(request_url, data={'username': username, 'password': password)

        request_url_2 = "https://web.housing.illinois.edu/MobileDining/WebService/MyBalances.asmx/CreateLongSession?k=d93b5fbd-d32c-4558-a5de-e9ab8dd6a31d-AITSWebService&netID=npant3" # build string
# GET /MobileDining/WebService/MyBalances.asmx/CreateLongSession?k=7A828F94-620B-4EE3-A56F-328036CC3C04&EASID=e5654b49-6458-41c3-b662-d76eed9dada5-AITSWebService&netID=npant3 HTTP/1.1
        # use same headers as above
        payload = { 'EASID': '', 'netID': username, 'k': '7A828F94-620B-4EE3-A56F-328036CC3C04' }
        requests.get(request_url_2)


# For dining/info endpoint: https://web.housing.illinois.edu/MobileDining/WebService/SettingTable.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04&t=json&ts=5-10-2012%2014:30:00
# for food: https://web.housing.illinois.edu/MobileDining/WebService/Search.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04&id=4&from=2015-11-16&to=2015-11-16&t=json


