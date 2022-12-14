import requests

def get_location(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}?fields=lat,lon,zip").json()
    return response
    

if __name__ == "__main__":
    print(get_location("138.199.40.168"))