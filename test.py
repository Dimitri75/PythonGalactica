import json
from pprint import pprint
json_data = open('cards.json')
data = json.load(json_data)
pprint(data)
json_data.close()