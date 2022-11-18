import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/my_cat"

resp = requests.get(URL)

pprint(resp.json())