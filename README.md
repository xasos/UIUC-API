# UIUC Open Data API

[![Build Status][travis-image]][travis-url] [![Requirements Status][require-image]][require-url]

Unofficial Open Data API for the University of Illinois at Urbana-Champaign. I'm building this out of frustration of not having a centralized data source for UIUC information. The idea was fleshed out [here](https://www.reddit.com/r/UIUC/comments/2hhlhn/would_anyone_be_interested_in_a_uiuc_open_data_api/
). This is still very much a WIP, so please feel free to submit an issue or contribute! The API is built with Python, Flask + [Flask RESTful](https://github.com/flask-restful/flask-restful), and Redis.

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
    "weather_condition": "",
    "temperature": "",
    "dew_point": "",
    "relative_humidity": "",
    "winds": "",
    "visibility": "",
    "pressure": "",
    "sunrise": "",
    "sunset": "",
    "images": [
      "latest_radar_image": "",
      "storm_total_precip_image": "",
      "surface_temp_image": "",
      "surface_dew_point_temp_image": "",
      "sea_level_pressure": "",
      "mdw_surface_observations": "",
      "composite_ir_image": "",
      "composite_enhanced_ir_image": ""
    ],
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

## newspaper


 
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
| uiuc-cli | CLI to university services | https://github.com/xasos/uiuc-api |
 
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
- teach kevin pls

## License
[MIT License](LICENSE)

throw in some redis/memcache for less server usage

[travis-url]: https://travis-ci.org/xasos/UIUC-Open-Data
[travis-image]: https://travis-ci.org/xasos/UIUC-Open-Data.svg?branch=master
[require-image]: https://requires.io/github/xasos/UIUC-Open-Data/requirements.svg?branch=master
[require-url]: https://requires.io/github/xasos/UIUC-Open-Data/requirements/?branch=master
[daviddm-url]: https://david-dm.org/xasos/Coins.svg?theme=shields.io
[daviddm-image]: https://david-dm.org/xasos/Coins
