from flask import Flask
from flask_restful import Resource, Api
from bs4 import BeautifulSoup
from IPython import embed
import urllib2

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Dining(Resource):
  def get(self):
    return {"yo": "ayy"}

class Weather(Resource):
  webpage = urllib2.urlopen('https://www.atmos.illinois.edu/weather/')
  soup = BeautifulSoup(webpage, "html.parser")
  embed()
  weather_startion_location = soup.find_all('font')[3]
  last_recorded_time = soup.find_all('font')[5]
  weather = 7 # in degrees farenheit
  hella_data = soup.find_all('font')[6]
  latestRadarImage = "https://www.atmos.illinois.edu/weather/tree/prods/current/nicerad/nicerad_N.gif"
  stormTotalPrecipImage = "https://www.atmos.illinois.edu/weather/tree/prods/current/niceradilxpretx/niceradilxpretx_N.gif"
  surfaceTempImage = "https://www.atmos.illinois.edu/weather/tree/prods/current/sfctmp/sfctmp_N.gif"
  surfaceDewPointTempImage = "https://www.atmos.illinois.edu/weather/tree/prods/current/sfctdp/sfctdp_N.gif"
  seaLevelPressure = "https://www.atmos.illinois.edu/weather/tree/prods/current/sfcslp/sfcslp_N.gif"
  mdwSufaceObservations = "https://www.atmos.illinois.edu/weather/tree/prods/current/sfcslp/sfcslp_N.gif"
  irImage = "https://www.atmos.illinois.edu/weather/tree/prods/current/satconusenhir/satconusenhir_N.gif"
  irImage2 = "https://www.atmos.illinois.edu/weather/tree/prods/current/satnoamir/satnoamir_N.gif"
  def get(self):
    return "yooo"


api.add_resource(HelloWorld, '/')
api.add_resource(Dining, '/dining')
api.add_resource(Weather, '/weather')

if __name__ == '__main__':
    app.run(debug=True)
