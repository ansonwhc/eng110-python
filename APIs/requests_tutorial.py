import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import json
from postcode import Postcode


response = requests.get("https://api.postcodes.io/postcodes/SE120NB")

if response.status_code == 200:
    content = response.json()
    # for k in ['eastings', 'northings']:
    #     print(content['result'][k])

    # soup = bs(response.text, 'html.parser')
    content_soup = bs(response.content, 'html.parser')


dict_data = {"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]}
json_data = json.dumps(dict_data)

response = requests.post(
    url="https://api.postcodes.io/postcodes",
    headers={"Content-Type": "application/json"},
    json=dict_data, # specifying data is in json format
    # data=json_data
)

if response.status_code == 200:
    content_json = response.json()
    for result in content_json['result']:

        postcode_class = Postcode(**result['result']) # <-
        print(postcode_class.region)

    #     ...print(the_others)

    # for query_result in content_json['result']:
    #     if query_result:
    #         pprint(query_result)
    #         result = query_result['result']
    #         postcode = result['postcode']
    #         region = result['region']
    #         pc = result['parliamentary_constituency']
    #         print(f"{postcode}: {region}, {pc}")
    #     else:
    #         print(f"{query_result['query']}: No postcode found")

