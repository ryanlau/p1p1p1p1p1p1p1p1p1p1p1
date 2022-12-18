import requests, json

with open("app/keys/key_nytimes.txt") as f:
    API_KEY = f.read().strip()


def get_news_list():
    response = requests.get(f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={API_KEY}").json()
    news_list = response["results"]
    return news_list

if __name__ == "__main__":
    print(get_news_list())