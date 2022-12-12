import requests


with open("app/keys/key_alpaca_id.txt") as f:
    API_KEY_ID = f.read().strip()

with open("app/keys/key_alpaca_secret.txt") as f:
    SECRET_KEY = f.read().strip()


headers = {
    "APCA-API-KEY-ID": API_KEY_ID,
    "APCA-API-SECRET-KEY": SECRET_KEY,
}


def get_snapshots(symbols: list[str]):
    prices = {}

    response = requests.get(f"https://data.alpaca.markets/v2/stocks/snapshots?symbols={','.join(symbols)}", headers=headers).json()

    for stock, data in response.items():
        prices[stock] = {}
        prices[stock]["price"] = round(data["latestTrade"]["p"], 2)
        prices[stock]["change"] = round(((data["latestTrade"]["p"] - data["prevDailyBar"]["c"]) / data["prevDailyBar"]["c"]) * 100, 2)

    return prices


def get_company_name(ticker):
    response = requests.get(f"https://paper-api.alpaca.markets/v2/assets/{ticker}", headers=headers)

    if response.status_code == 404:
        return None

    return response.json()["name"]


if __name__ == "__main__":
    print(get_snapshots(["AAPL", "AMZN"]))
    print(get_company_name("AAPL"))
    print(get_company_name("FORtnITE"))

