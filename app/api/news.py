import requests, json

with open("app/keys/key_nytimes.txt") as f:
    API_KEY = f.read().strip()

response = requests.get(f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={API_KEY}").json()
# print(response)
news_list = response["results"]

def get_news_list():
    return news_list

def get_news_title(i):
    return news_list[i]["title"]

def get_news_blurb(i):
    return news_list[i]["abstract"]

def get_news_url(i):
    return news_list[i]["url"]

def get_news_img(i):
    return news_list[i]["multimedia"][0]["url"]

if __name__ == "__main__":
    print(get_news_title(0))
    print(get_news_blurb(0))
    print(get_news_url(0))
    print(get_news_img(0))