import requests, json, random


with open("app/keys/key_favQs.txt") as f:
    API_KEY_ID = f.read().strip()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token token={API_KEY_ID}",
}

def get_qotd():
    response = requests.get("https://favqs.com/api/quotes?filter=inspirational&type=tag", headers=headers).json()
    #print(response)
    rand = random.randint(0,len(response["quotes"]))
    quote_body = response["quotes"][rand]["body"]
    quote_author = response["quotes"][rand]["author"]
    return (f"{quote_body} ~ {quote_author}")

# LINES BELOW ONLY GET RUN IF "EXPLICITY RAN" with `python3 app/api/favQs.py`
if __name__ == "__main__":
    print(get_qotd())
