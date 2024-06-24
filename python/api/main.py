import requests
import json
import ast
import pandas as pd
from pprint import pprint

parameters = {"@authtoken": "6l8V4c0v0Q4x3x3Y1y9n", "PortId":"sftpNestle"}

response = requests.get("http://202.53.225.252:5443/rssbus/api.rsc/transactions/", params=parameters)
json_response = response.json()
text_response = response.text

f = open('jsonlog','w')

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text, file=f)

pprint(json_response)

# print(json_response, file=f)
# val = ast.literal_eval(json_response)
# val1 = json.loads(json.dumps(val))