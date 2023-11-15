from tinydb import TinyDB, Query


db = TinyDB('./src/Database/forms.json')
db.insert_multiple([
  {
    "name": "VITRICOMP",
    "address": "773 Trucklemans Lane, Wollochet, Federated States Of Micronesia, 298",
    "birthday": "2014-07-27"
  },
  {
    "name": "TALENDULA",
    "address": "797 Seigel Street, Noblestown, New Hampshire, 1524",
    "birthday": "2022-11-15"
  },
  {
    "name": "COMSTRUCT",
    "address": "876 Bartlett Street, Dola, Maryland, 2424",
    "birthday": "2021-07-13"
  },
  {
    "name": "PROWASTE",
    "email": "lavernemullins@prowaste.com",
    "phone": "+7 830 442 38 05",
    "address": "850 Farragut Place, Hailesboro, Illinois, 6030",
    "date": "2014-01-09"
  },
  {
    "name": "DYNO",
    "email": "lavernemullins@dyno.com",
    "phonsae": "+7 843 589 39 42",
    "addddress": "397 Seagate Avenue, Callaghan, Hawaii, 1801",
    "date": "2023-09-07"
  },
  {
    "name": "QUALITEX",
    "email": "lavernemullins@qualitex.com",
    "phonsae": "+7 871 592 33 94",
    "addddress": "550 Cedar Street, Oretta, Arkansas, 8136",
    "date": "2020-10-02"
  },
  {
    "name": "COMBOGENE",
    "email": "lavernemullins@combogene.com",
    "phonsae": "+7 834 433 33 43",
    "addddress": "189 Newton Street, Conestoga, Missouri, 2524",
    "date": "2018-03-16"
  },
  {
    "name": "BLUEGRAIN",
    "email": "lavernemullins@bluegrain.com",
    "phonsae": "+7 896 533 32 32",
    "addddress": "881 Winthrop Street, Abiquiu, Arizona, 4765",
    "date": "2022-06-16"
  },
])