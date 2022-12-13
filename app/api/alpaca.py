import requests
from datetime import date


with open("app/keys/key_alpaca_id.txt") as f:
    API_KEY_ID = f.read().strip()

with open("app/keys/key_alpaca_secret.txt") as f:
    SECRET_KEY = f.read().strip()


headers = {
    "APCA-API-KEY-ID": API_KEY_ID,
    "APCA-API-SECRET-KEY": SECRET_KEY,
}


def get_last_trading_day():
    response = requests.get(f"https://paper-api.alpaca.markets/v2/calendar?end={date.today()}", headers=headers).json()

    last = response[-1]
    day = last["date"]

    o = f"{day}T{last['open']}:00-05:00"
    c = f"{day}T{last['close']}:00-05:00"

    return (o, c)


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


def get_daily_bars(tickers: list[str]):
    day = get_last_trading_day()
    response = requests.get(f"https://data.alpaca.markets/v2/stocks/bars?symbols={','.join(tickers)}&timeframe=2Min&start={day[0]}&end={day[1]}", headers=headers).json()
    response = response["bars"]

    bars_d = {}

    for stock, bars in response.items():
        cleaned_bars = []
        for bar in bars:
            cleaned_bars.append({"x": bar["t"], "y": bar["vw"]})

        bars_d[stock] = cleaned_bars

    return bars_d


if __name__ == "__main__":
    print(get_snapshots(["BRK.A", "AMZN"]))
    print(get_company_name("AAPL"))
    print(get_company_name("FORtnITE"))
    print(get_daily_bars(["AAPL", "AMZN"]))
    print(get_last_trading_day())

