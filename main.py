import requests
import json
#from bs4 import BeautifulSoup
import pandas as pd

api_url = "https://api.flightradar24.com/common/v1/airport.json"
parameters = {
    "code": "MUC",
    "limit": 100
}

response = requests.get("https://api.flightradar24.com/common/v1/airport.json", parameters)
# response.raise_for_status()
if response.status_code == "200":
    data = response.json()
    question_data = data["results"]
else:
    data=pd.read_html(api_url)