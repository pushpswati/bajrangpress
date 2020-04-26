
import requests


URL="https://api.coronatracker.com/v3/stats/worldometer/country?countryCode=IN"

Location="corona_data"
PARAMS={"ADDRESS":"Location"}

r=requests.get(url=URL,params=PARAMS)
data=r.json()



API_ENDPOINT="http://34.206.109.62:8000/coronatracker/"

  
# data to be sent to api 
payload =data[0]


r = requests.post(url = API_ENDPOINT, data = payload) 
  
# extracting response text  

pastebin_url = r.text 
print(pastebin_url)
