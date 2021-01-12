import requests 

BASE = "http://127.0.0.1:5000/"

payload = {
    "Currency Names" : ['EUR', 'USD'],
    "Exchange Rates" : { 0 : [1, 1.16], 1 : [0.95, 1] }
}
post_response = requests.post(BASE + "exchangeRates/1", json=payload)
print(post_response.json())

get_response = requests.get(BASE + "exchangeRates/1")
print(get_response.json())