# University of Illinois at Urbana-Champaign Open Data API

[![Build Status][travis-image]][travis-url] [![Dependency Status][daviddm-url]][daviddm-image]

Unofficial Open Data API for UIUC. Heavily Modeled off of the University of Waterloo [Open Data API](https://github.com/uWaterloo/api-documentation/). I'm building this out of frustration of not having a centralized data source for UIUC information. This is still very much a WIP, so please feel free to submit an issue or contribute!

## Usage
**Base URL:** http://uiuc-api.herokuapp.com

**Output:** JSON

## Dining Services

Get information about food from all dorms.

#### `GET /coins`

Example Query:
```
http://coins-api.herokuapp.com/coins
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

### Dining Services (https://web.housing.illinois.edu/MobileDining/WebService/SettingTable.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04&t=json&ts=5-10-2012%2014:30:00)
 - /dining/menu
 - /dining/halls
 - /dining/{year}/{week}/menu

### Weather
 - /weather

### Course Information

### University Directory
 - /directory/search/:searchType/:query
 - 
 
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
 
## Statistics
So far, x users have used the API and over y requests have been made!

## Disclaimer
Use of this API

## License
[MIT License](LICENSE)


[travis-url]: https://travis-ci.org/xasos/Coins
[travis-image]: https://travis-ci.org/xasos/Coins.svg?branch=master
[daviddm-url]: https://david-dm.org/xasos/Coins.svg?theme=shields.io
[daviddm-image]: https://david-dm.org/xasos/Coins
