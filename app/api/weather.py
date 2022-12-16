import requests

with open("app/keys/key_openweathermap.txt") as f:
    API_KEY = f.read().strip()

def get_current(lat,lon):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial")
    des = response.json()["weather"][0]["description"] 
    temp = response.json()["main"]["temp"]
    sunrise = response.json()["sys"]["sunrise"]
    sunset = response.json()["sys"]["sunset"]
    timezone = response.json()["timezone"]
    l = [des,temp,sunrise+timezone,sunset+timezone]
    return l
    
def convert(zip):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/zip?zip={zip},US&appid={API_KEY}")
    lat = response.json()["lat"]
    lon = response.json()["lon"]
    return (lat,lon)

def get_four(q,cnt):
    response = requests.get(f"https://pro.openweathermap.org/data/2.5/forecast/hourly?q={q}&cnt={cnt}&appid={API key}")
    a = response.json()["temp"]["day"]
    return a

if __name__ == "__main__":
    zip = 10282
    coords = convert(zip)
    print(get_current(coords[0], coords[1]))