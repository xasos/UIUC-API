from flask import Flask
from flask_restful import Api
from myapi.resources.dining import Dining
from myapi.resources.weather import Weather
from myapi.resources.wifi import Wifi
from myapi.resources.laundry import Laundry

app = Flask(__name__)
api = Api(app)

api.add_resource(Dining, '/dining/search/<query>', '/dining/<hall>/<dateFrom>/<dateTo>')
api.add_resource(Weather, '/Bar', '/Bar/<str:id>')
api.add_resource(Wifi, '/Baz', '/Baz/<str:id>')
#api.add_resource(Laundry, '', '')
#api.add_resource(UniversityDirectory, '', '')
#api.add_resource(DailyIllini, '', '')
#api.add_resource(Buildings, '', '')
#api.add_resource(AthleticSchedule, '', '')
#api.add(Maintenance, '', '')
