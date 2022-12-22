# ohayo by FORTNITE

## Roster

* Ryan Lau
* Craig Chen
* Elizabeth Paperno
* Hui Wang

## App Description

A personal dashboard to keep your life in order! 

On the dashboard, we will display the weather, sunrise/sunset time, stock data, an inspirational quote for the day, a list of news articles, and an area to write to-do items. Each widget will link to a page that displays more in-depth information when clicked on by the user. 

## APIs Used
#### [Alpaca Market Data API (stocks)](https://alpaca.markets/docs/api-references/market-data-api/stock-pricing-data/historical/)
[Card](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_AlpacaMarketData.md)


#### [Open Weather Map API (weather)](https://openweathermap.org/api)
[Card](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_OpenWeather.md)

[**IMPORTANT REGARDING OPENWEATHER**](https://github.com/ryanlau/p1p1p1p1p1p1p1p1p1p1p1/blob/main/app/keys/readme)

#### [Fav Qs API (qotd)](https://favqs.com/api)
[Card](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411FavQs.md)

#### [New York Times API (news)](https://developer.nytimes.com/apis)
[Card](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_NYTMostPopular.md)


## Launch Codes

0. Clone repo

```bash
git clone https://github.com/ryanlau/p1p1p1p1p1p1p1p1p1p1p1.git
```

1. `cd` into local repo

```bash
cd p1p1p1p1p1p1p1p1p1p1p1
```

2. Optionally, create and activate a new virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

3. Install required packages

```bash
pip install -r requirements.txt
```

4. Start Flask server

```bash
python app/__init__.py
```

5. Visit `http://127.0.0.1:5000/` in browser
