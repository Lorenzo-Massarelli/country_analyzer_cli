import requests

URL = "https://restcountries.com/v3.1/all"
FIELDS = "name,population,region,capital,languages,currencies,area"

def fetch_countries():
    try:
        r=requests.get(URL, params={"fields": FIELDS}, timeout=10)  
        r.raise_for_status()
        return r.json()
    
    except requests.exceptions.RequestException:
        return []