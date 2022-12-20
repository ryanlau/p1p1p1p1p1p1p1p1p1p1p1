import requests
from datetime import date, datetime, timedelta


with open("app/keys/key_alpaca_id.txt") as f:
    API_KEY_ID = f.read().strip()

with open("app/keys/key_alpaca_secret.txt") as f:
    SECRET_KEY = f.read().strip()


headers = {
    "APCA-API-KEY-ID": API_KEY_ID,
    "APCA-API-SECRET-KEY": SECRET_KEY,
}

'''
def is_market_day():
    today = date.today()
    
    response = requests.get(f"https://paper-api.alpaca.markets/v2/calendar?end={today}", headers=headers).json()

    last = response[-1]
    last = datetime.strptime(last["date"], "%Y-%m-%d")

    return last.day == today.day
'''

def get_market_calendar():
    calendar = requests.get(f"https://paper-api.alpaca.markets/v2/calendar?end={date.today()}", headers=headers).json()
    return calendar 


def is_market_open(calendar):
    last = calendar[-1]
    day = last["date"]

    o = f"{day}T{last['open']}:00"
    c = f"{day}T{last['close']}:00"

    o = datetime.strptime(o, "%Y-%m-%dT%H:%M:%S") + timedelta(hours=5)
    c = datetime.strptime(c, "%Y-%m-%dT%H:%M:%S") + timedelta(hours=5)

    t = datetime.utcnow()

    if o < t and c > t:
        return True

def get_last_started_trading_day(calendar):
    last = calendar[-1]
    day = last["date"]

    o = f"{day}T{last['open']}:00"

    d1 = datetime.strptime(o, "%Y-%m-%dT%H:%M:%S") + timedelta(hours=5)

    if d1 > datetime.utcnow(): # trading day has not started:
        last = calendar[-2]
        day = last["date"]

    o = f"{day}T{last['open']}:00-05:00"
    c = f"{day}T{last['close']}:00-05:00"

    return (o, c)


def get_snapshots(symbols):
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


def get_daily_bars(tickers):
    bars_d = {}

    calendar = get_market_calendar()
    day = get_last_started_trading_day(calendar)

    if is_market_open(calendar):
        response = requests.get(f"https://data.alpaca.markets/v2/stocks/bars?symbols={','.join(tickers)}&timeframe=12Min&start={day[0]}", headers=headers)
    else:
        response = requests.get(f"https://data.alpaca.markets/v2/stocks/bars?symbols={','.join(tickers)}&timeframe=12Min&start={day[0]}&end={day[1]}", headers=headers)

    print(response.url)
    response = response.json().get("bars")

    if response:
        for stock, bars in response.items():
            cleaned_bars = []
            for bar in bars:
                cleaned_bars.append({"x": bar["t"], "y": bar["vw"]})

            bars_d[stock] = cleaned_bars

    return bars_d


if __name__ == "__main__":
    calendar = get_market_calendar()
    print(is_market_open(calendar))
    print(get_last_started_trading_day(calendar))
    print(get_snapshots(["AAPL", "AMZN"]))
    print(get_company_name("AAPL"))
    print(get_company_name("FORtnITE"))
    print(get_daily_bars(["AAPL", "AMZN"]))

