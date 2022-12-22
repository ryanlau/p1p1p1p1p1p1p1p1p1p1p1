import requests, json
from datetime import datetime

with open("app/keys/key_openweathermap.txt") as f:
    API_KEY = f.read().strip()

# def get_current_for_zip(zip):
#     coords = get_coords_from_zip(zip)
#     response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={coords[0]}&lon={coords[1]}&appid={API_KEY}&units=imperial").json()
#     return response
    
def get_coords_from_zip(zip):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/zip?zip={zip},US&appid={API_KEY}").json()
    
    if response.get("cod") == "404":
        return None

    return response

def get_next_five(lat, lon):
    response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial&exclude=minutely,hourly,alerts").json()

    for i in range(len(response.get("daily"))):
        response["daily"][i]["dow"] = datetime.fromtimestamp(response["daily"][i]["dt"]).strftime("%a")
        # print(response["daily"][i]["dow"])
        

    return response


if __name__ == "__main__":
    coords = get_coords_from_zip(10282)
    print(json.dumps(get_next_five(coords["lat"], coords["lon"]), indent=4))