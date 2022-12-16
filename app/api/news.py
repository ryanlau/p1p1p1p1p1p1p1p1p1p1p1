import requests, json

with open("app/keys/key_nytimes_api.txt") as f:
    API_KEY = f.read().strip()

response = requests.get(f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={API_KEY}")

def get_news_title():
    return response["0"]["title"]

def get_news_blurb():
    return response["0"]["abstract"]

def get_news_url():
    return response["0"]["url"]

def get_news_img():
    return response["0"]["multimedia"]["1"]["url"]

if __name__ == "__main__":
    print(get_news_title())
    print(get_news_blurb())
    print(get_news_url())
    print(get_news_img())