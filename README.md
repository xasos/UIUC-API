# UIUC Open Data API

[![Join the chat at https://gitter.im/xasos/UIUC-Open-Data](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/xasos/UIUC-Open-Data?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

<!--[![Build Status][travis-image]][travis-url] [![Requirements Status][require-image]][require-url]-->

Unofficial Open Data API for the University of Illinois at Urbana-Champaign. Provides data for various services on campus such as Dining, Weather, Wi-Fi, etc. The API is built with Python, Flask + [Flask RESTful](https://github.com/flask-restful/flask-restful), and Redis. Interest in the project was gauged [here](https://www.reddit.com/r/UIUC/comments/2hhlhn/would_anyone_be_interested_in_a_uiuc_open_data_api/
). This is still very much a WIP, so please feel free to [submit an issue](https://github.com/xasos/UIUC-Open-Data/issues/new) or [contribute](https://github.com/xasos/UIUC-Open-Data/blob/master/CONTRIBUTING.md)!

*Note: This is an unofficial API and is not supported or controlled by the University of Illinois at Urbana-Champaign itself. Any questions, comments, feedback or feature requests should be directed to xasos or via an issue in this repo.*

## Usage
**Base URL:** http://uiuc-api.herokuapp.com

**Output:** JSON

## Dining Services

Get information about food options from all dining halls.

#### `GET /dining`

Example Query:
```
http://uiuc-api.herokuapp.com/dining
```

Response:
```json
  {
    "name": "bitcoin",
    "position": "1",
    "price": "356.51",
    "marketCap": "4847623128",
    "ticker": "BTC",
    "volume": "29824000",
    "delta24hr": "2.37",
    "timestamp": 1418325595612,
    "currency": "usd"
  },
  {
    "name": "ripple",
    "position": "2",
    "price": "0.016374",
    "marketCap": "505654484",
    "ticker": "XRP",
    "volume": "1620910",
    "delta24hr": "6.48",
    "timestamp": 1418325595612,
    "currency": "usd"
  },
  ...
  ...
```

## Weather

Get weather information from the [Department of Atmospheric Sciences](https://www.atmos.illinois.edu/weather/).

#### `GET /weather`

Example Query:
```
http://uiuc-api.herokuapp.com/weather
```

Response:
```json
  {
    "weather_station_location": "Willard Airport",
    "last_recorded_time": "1446098674",
    "weather_condition": "Cloudy Skies",
    "temperature": "54",
    "dew_point": "45",
    "relative_humidity": "71%",
    "winds": "NW at 17 mph",
    "visibility": "10 miles",
    "pressure": "1020.0 mb (30.13 in)",
    "sunrise": "7:13AM", 
    "sunset": "6:01PM",
    "images": {
      "latest_radar_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/nicerad/nicerad_N.gif",
      "storm_total_precip_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/niceradilxpretx/niceradilxpretx_N.gif",
      "surface_temp_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/sfctmp/sfctmp_N.gif",
      "surface_dew_point_temp_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/sfctdp/sfctdp_N.gif",
      "sea_level_pressure": "https://www.atmos.illinois.edu/weather/tree/prods/current/sfcslp/sfcslp_N.gif",
      "mdw_surface_observations": "https://www.atmos.illinois.edu/weather/tree/prods/current/sfcslp/sfcslp_N.gif",
      "composite_ir_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/satconusenhir/satconusenhir_N.gif",
      "composite_enhanced_ir_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/satnoamir/satnoamir_N.gif"
    },
    "": ""
  }
```

## Wi-Fi

Get Wi-Fi information for various places around campus.

#### `GET /wifi`

Example Query:
```
http://uiuc-api.herokuapp.com/wifi
```

Response:
```json
  {
    "weather_station_location": "Willard Airport"
  }
```

### Dining Services (https://web.housing.illinois.edu/MobileDining/WebService/SettingTable.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04&t=json&ts=5-10-2012%2014:30:00)
 - /dining/menu
 - /dining/halls
 - /dining/{year}/{week}/menu\

### Course Information

### University Directory
 - /directory/search/:searchType/:query
 - 
 
## Faculty

## The Daily Illini

## Transportation
The Champaign-Urbana Mass Transit District offers an [API](https://developer.cumtd.com/) for transporation information in Champaign-Urbana. There are several API wrappers and Open-source apps written with the CUMTD API on [GitHub](https://github.com/search?utf8=%E2%9C%93&q=cumtd) as well as in their [App Garage](http://www.cumtd.com/maps-and-schedules/app-garage).
 
## Run Locally
```sh
$ pip install -r requirements.txt
$ python api.py
```

## Deploy to Heroku 
```sh
$ pip install -r requirements.txt
$ heroku create
$ (git add, git commit)
$ git push heroku master
```


## Client Libraries
 - []() (Python)
 - []() (Node.js)
 - []() (Java)
 - 
 
## Expo
Some apps built using this API - if you've built an app using this API, feel free to add it by sending a PR!

| Name | Description | URL |
| ---- | ---- | ---- |
| uiuc-cli | CLI to university services | https://github.com/xasos/uiuc-cli |
 
## Statistics
So far, x users have used the API and over y requests have been made!

## Disclaimer
Use of this API

## Todo
- contributing.md
- front-end
- cli
- client libraries
- meal credits (untested)
- transportation
- generate google calendar
- uiuc calendar
- teach kevin pls
- department events/seminars
- wiki
- buildings
- Networking, Lens API 
- https://techservices.illinois.edu/services/campus-lightweight-directory-access-protocol
- to do list
- document (hehehehe) code
- 
## Contributing
[Contributing 

## License
[MIT License](LICENSE)

throw in some redis/memcache for less server usage

[travis-url]: https://travis-ci.org/xasos/UIUC-Open-Data
[travis-image]: https://travis-ci.org/xasos/UIUC-Open-Data.svg?branch=master
[require-image]: https://requires.io/github/xasos/UIUC-Open-Data/requirements.svg?branch=master
[require-url]: https://requires.io/github/xasos/UIUC-Open-Data/requirements/?branch=master
[daviddm-url]: https://david-dm.org/xasos/Coins.svg?theme=shields.io
[daviddm-image]: https://david-dm.org/xasos/Coins
