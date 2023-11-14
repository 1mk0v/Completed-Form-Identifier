from tinydb import TinyDB, Query


db = TinyDB('./src/Database/forms.json')
db.insert_multiple([
  {
    "name": "VITRICOMP",
    "email": "lavernemullins@vitricomp.com",
    "phone": "+7 (862) 539-2249",
    "address": "773 Trucklemans Lane, Wollochet, Federated States Of Micronesia, 298",
    "date": "2014-07-27"
  },
  {
    "name": "TALENDULA",
    "email": "lavernemullins@talendula.com",
    "phone": "+7 (849) 402-2059",
    "address": "797 Seigel Street, Noblestown, New Hampshire, 1524",
    "date": "2022-11-15"
  },
  {
    "name": "COMSTRUCT",
    "email": "lavernemullins@comstruct.com",
    "phone": "+7 (970) 596-2684",
    "address": "876 Bartlett Street, Dola, Maryland, 2424",
    "date": "2021-07-13"
  },
  {
    "name": "PROWASTE",
    "email": "lavernemullins@prowaste.com",
    "phone": "+7 (830) 442-3805",
    "address": "850 Farragut Place, Hailesboro, Illinois, 6030",
    "date": "2014-01-09"
  },
  {
    "name": "DYNO",
    "email": "lavernemullins@dyno.com",
    "phone": "+7 (843) 589-3942",
    "address": "397 Seagate Avenue, Callaghan, Hawaii, 1801",
    "date": "2023-09-07"
  },
  {
    "name": "QUALITEX",
    "email": "lavernemullins@qualitex.com",
    "phone": "+7 (871) 592-3394",
    "address": "550 Cedar Street, Oretta, Arkansas, 8136",
    "date": "2020-10-02"
  },
  {
    "name": "COMBOGENE",
    "email": "lavernemullins@combogene.com",
    "phone": "+7 (834) 433-3343",
    "address": "189 Newton Street, Conestoga, Missouri, 2524",
    "date": "2018-03-16"
  },
  {
    "name": "BLUEGRAIN",
    "email": "lavernemullins@bluegrain.com",
    "phone": "+7 (896) 533-3232",
    "address": "881 Winthrop Street, Abiquiu, Arizona, 4765",
    "date": "2022-06-16"
  },
  {
    "index": 0,
    "isActive": True,
    "balance": "$1,435.94",
    "name": "PREMIANT",
    "registered": "2022-10-14"
  },
  {
    "index": 1,
    "isActive": False,
    "balance": "$3,071.72",
    "name": "ARTIQ",
    "registered": "2016-05-04"
  },
  {
    "index": 2,
    "isActive": False,
    "balance": "$1,944.22",
    "name": "INFOTRIPS",
    "registered": "2021-06-22"
  },
  {
    "index": 3,
    "isActive": False,
    "balance": "$3,947.56",
    "name": "ZIALACTIC",
    "registered": "2018-05-24"
  },
  {
    "index": 4,
    "isActive": True,
    "balance": "$2,603.55",
    "name": "FILODYNE",
    "registered": "2020-07-19"
  },
  {
    "index": 5,
    "isActive": True,
    "balance": "$3,990.43",
    "name": "HINWAY",
    "registered": "2021-04-01"
  },
  {
    "index": 6,
    "isActive": False,
    "balance": "$2,175.07",
    "name": "FOSSIEL",
    "registered": "2022-05-11"
  },
  {
    "index": 7,
    "isActive": False,
    "balance": "$3,676.70",
    "name": "COMSTAR",
    "registered": "2018-04-06"
  },
  {
    "index": 8,
    "isActive": True,
    "balance": "$3,067.89",
    "name": "MANUFACT",
    "registered": "2019-04-11"
  }
])