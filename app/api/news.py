import requests, json

with open("app/keys/key_nytimes.txt") as f:
    API_KEY = f.read().strip()

response = requests.get(f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={API_KEY}").json()
# print(response)
news_list = response["results"]

def get_news_list():
    return news_list

if __name__ == "__main__":
    print(news_list)