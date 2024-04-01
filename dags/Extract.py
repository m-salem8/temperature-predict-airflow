import requests 
import json
from datetime import datetime

################################# API Settings ##################################
key = '8b5e13e654e2b306506a5b5e35c6bbf8'
API_key=key
cities =['Paris', 'London', 'Washington']

# function to retieve the data from the API
def get_data(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch data for city: {city}. Error:{e}")

# Function to save the data for a city locally in app/raw_files/
def save_data(data, timestamp):
    filenme = f"/app/raw_files/{timestamp}.json"
    with open(filenme, 'w') as file:
        json.dump(data, file, indent=4)

# Function to ge the data for the 3 cities and store them 
def extract():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    all_cities = {}
    for city in cities:
        all_cities[city]=get_data(city)
    save_data(all_cities, timestamp)

if __name__=="__main__":
    extract()
