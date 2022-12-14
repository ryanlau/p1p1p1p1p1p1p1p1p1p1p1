import requests, json

with open("app/keys/key_favQs.txt") as f:
    API_KEY_ID = f.read().strip()

def get_qotd():
    response = requests.get("https://favqs.com/api/qotd").json()
    #print(response)
    quote_body = response["quote"]["body"]
    quote_author = response["quote"]["author"]
    return (f"{quote_body} ~ {quote_author}")

# LINES BELOW ONLY GET RUN IF "EXPLICITY RAN" with `python3 app/api/favQs.py`
if __name__ == "__main__":
    print(get_qotd())
