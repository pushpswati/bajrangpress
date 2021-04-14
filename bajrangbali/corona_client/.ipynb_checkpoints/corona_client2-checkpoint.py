import requests

URL="https://api.coronatracker.com/v3/stats/worldometer/topCountry?limit=15&sort=-confirmed"



r=requests.get(url=URL)
data=r.json()

API_ENDPOINT="http://34.206.109.62:8000/coronatracker/"


for payload in data: 
    r = requests.post(url = API_ENDPOINT, data = payload) 
  
     # extracting response text  

    response_data = r.text 
    print("The response_data is:%s"%response_data) 