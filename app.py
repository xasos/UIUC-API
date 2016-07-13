from flask import Flask
from flask_restful import Api, Resource
from werkzeug.contrib.cache import SimpleCache

from resources.dining import Dining, DiningInformation, DiningSearch, DiningToday
from resources.weather import Weather
from resources.wifi import Wifi, WifiNearMe
from resources.laundry import Laundry
from resources.main import Main
from resources.free_food import FreeFood
from resources.ews_status import EWSStatus
from resources.athletic_schedule import AthleticSchedule
from resources.buildings import Buildings
from resources.directory import FacultyDirectory
from resources.daily_illini import News, SubCategoryNews, SportsNews, RecentNews

app = Flask(__name__)
api = Api(app)
cache = SimpleCache(app)

# Define routes
api.add_resource(Main, '/')

#api.add_resource(Dining, '/dining/search/<query>', '/dining/<hall>/<dateFrom>/<dateTo>', '/dining/information', '/dining/balance')
'''Dining'''
api.add_resource(DiningToday, '/dining/<string:hall>')
api.add_resource(Dining, '/dining/<string:hall>/<string:dateFrom>/<string:dateTo>')
api.add_resource(DiningSearch, '/dining/search/<string:query>')
api.add_resource(DiningInformation, '/dining/information')

'''Wifi'''
#api.add_resource(Wifi, '/wifi')
#api.add_resource(WifiNearMe, '/wifi/<string:latitude>/<string:longitude>')

api.add_resource(Weather, '/weather')

api.add_resource(Laundry, '/laundry')

api.add_resource(FacultyDirectory, '/directory/faculty')

'''News'''
api.add_resource(News, '/news/<string:category>')
api.add_resource(SubCategoryNews, '/news/<string:category>/<string:subcategory>')
api.add_resource(SportsNews, '/news/<string:category>/<string:subcategory>/<string:sportcategory>')
api.add_resource(RecentNews, '/news/recent')

api.add_resource(Buildings, '/buildings')

api.add_resource(AthleticSchedule, '/athleticschedule/<string:sport>')

#api.add(Maintenance, '', '')

api.add_resource(FreeFood, '/freefood')

api.add_resource(EWSStatus, '/ews-status')

if __name__ == '__main__':
    app.run(debug=True)
