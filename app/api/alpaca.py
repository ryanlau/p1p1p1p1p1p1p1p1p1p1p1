import requests


with open("app/keys/key_alpaca_id.txt") as f:
    API_KEY_ID = f.read().strip()

with open("app/keys/key_alpaca_secret.txt") as f:
    SECRET_KEY = f.read().strip()


headers = {
    "APCA-API-KEY-ID": API_KEY_ID,
    "APCA-API-SECRET-KEY": SECRET_KEY,
}


def get_prices(stocks):
    d = {}

    response = requests.get(f"https://data.alpaca.markets/v2/stocks/quotes/latest?symbols={','.join(symbols)}", headers=headers)
    response = response.json()


    quotes = response.get("quotes")

    for stock, data in quotes.values():
        d[stock] = data["ap"]

    return d
