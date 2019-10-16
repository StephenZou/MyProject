# This is where you define the models of your application.
# This may be split into several modules in the same way as views.py.
import requests
import json


def resolve(data):
    uri_base = "http://127.0.0.1:9090/ltp"
    data = {'s': data, 'x': 'n', 't': 'srl'}
    response = requests.get(uri_base, data=data)
    rcdata = response.json()
    print(json.dumps(rcdata, indent=4, ensure_ascii=False))
    return rcdata
