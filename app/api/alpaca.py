import requests


with open("app/keys/key_alpaca_id.txt") as f:
    API_KEY_ID = f.read().strip()

with open("app/keys/key_alpaca_secret.txt") as f:
    SECRET_KEY = f.read().strip()


headers = {
    "APCA-API-KEY-ID": API_KEY_ID,
    "APCA-API-SECRET-KEY": SECRET_KEY,
}


def get_prices(symbols: list[str]):
    prices = {}

    response = requests.get(f"https://data.alpaca.markets/v2/stocks/quotes/latest?symbols={','.join(symbols)}", headers=headers).json()

    quotes = response.get("quotes")

    for stock, data in quotes.items():
        prices[stock] = data["ap"]

    return prices


if __name__ == "__main__":
    print(get_prices(["AAPL", "AMZN"]))
