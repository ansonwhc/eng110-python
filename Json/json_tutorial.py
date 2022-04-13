import json


car = {"make": "tesla",
       "engine": "electric",
       "faults": "lots",
       "is_expensive": True,
       "driver": None}

# with open("car_json_file.json", "w") as jsonfile:
#     json.dump(car, jsonfile)

# with open("new_car_json_file.json", 'r') as jsonfile: # manually edited
#     new_car = json.load(jsonfile)
#
# print(new_car, type(new_car))

detail = {"Name": "Anson",
          "Age": 23,
          "Langauge": ['English',
                       'Cantonese',
                       'Mandarin Chinese',
                       'German',
                       'Polish']}

with open("details.json", 'w') as wf:
    json.dump(detail, wf)

with open("details.json", 'r') as rf:
    detail_loaded = json.load(rf)

print(detail == detail_loaded)

# API ==> Application programme interface
