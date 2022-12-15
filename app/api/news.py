import requests, json

with open("app/keys/key_nytimes_api.txt") as f:
    API_KEY = f.read().strip()

def get_news():
    response = requests.get(f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={API_KEY}")
    news_title = response["0"]["title"]
    news_blurb = response["0"]["abstract"]
    news_url = response["0"]["url"]
    news_img = response["0"]["multimedia"]["1"]["url"]
    n = (f"{news_title} ~ {news_blurb} ~ {news_img} ~ {news_img}")
    return n

if __name__ == "__main__":
    print(get_news())