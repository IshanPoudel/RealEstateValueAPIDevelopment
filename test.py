import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "getvalue")

print(response.json())


#json python dictionaries ,