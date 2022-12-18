import requests, json

with open("app/keys/key_nytimes_api.txt") as f:
    API_KEY = f.read().strip()

response = requests.get(f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={API_KEY}").json()
# print(response)
news = response["results"][0]

def get_news_title():
    return news["title"]

def get_news_blurb():
    return news["abstract"]

def get_news_url():
    return news["url"]

def get_news_img():
    return news["multimedia"][0]["url"]

if __name__ == "__main__":
    print(get_news_title())
    print(get_news_blurb())
    print(get_news_url())
    print(get_news_img())