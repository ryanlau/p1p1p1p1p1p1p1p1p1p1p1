import requests

with open("app/keys/key_openweathermap.txt") as f:
    API_KEY = f.read().strip()

def get_current(lat,lon):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial")
    return [response.json["main"]["temp"],response.json["weather"]["main"]]
    

if __name__ == "__main__":
    lat = "40.717831142775566" 
    lon = "-74.0137791697529"
    print(get_current(lat, lon))