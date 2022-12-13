# FORTNITE: Ryan Lau, Craig Chen, Elizabeth Paperno, Hui Wang
# SoftDev
# p1: ohayo
# 2022-12-07
# time spent: 3.0 hrs


from flask import Flask, render_template, request, session, flash, redirect
from functools import wraps
import secrets
import json

from db import auth, todo, watchlists

from api import alpaca


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = session.get("username")
        if username is None:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function

app = Flask(__name__) #create instance of class Flask


@app.route('/')
def index():
    username = session.get("username")

    if username is None:
        return render_template('login.html')

    # TODO: FETCH FOLLOWING DATA FROM DB
    stocks = watchlists.get_watchlist(username)

    stock_data = {}
    if len(stocks) > 0:
        stock_data = alpaca.get_snapshots([stock[0] for stock in stocks])
        bars = alpaca.get_daily_bars([stock[0] for stock in stocks])

        for stock in stocks:
            stock_data[stock[0]]["name"] = stock[1]
            stock_data[stock[0]]["bars"] = bars[stock[0]]

    return render_template('dashboard.html', stock_data=stock_data, username=session['username'])

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    info_correct = auth.check_creds(username, password)

    if info_correct:
        session['username'] = username
    else:
        flash("invalid username or password")

    return redirect("/")

# @app.route("/register",methods=['POST'])
# def register():
#     if request.method == 'POST':    
#         key = get_random_string()
#         username = str(request.form.get('username'))
#         password = str(request.form.get('password'))
        
#         command = f"insert into users values('{username}','{password}');"
#         db.execute(command)
        
#     file.commit()
    
#     session["username"]= username
#     session["password"]=password

#     return render_template('register.html')
    
    
@app.route("/stocks")
@login_required
def stocks():
    return render_template('stocks.html')


@app.route("/weather")
@login_required
def weather():
    return render_template('weather.html')


@app.route("/news")
@login_required
def news():
    return render_template('news.html')


@app.route("/todos")
@login_required
def todo():
    return render_template('todos.html')


@app.route("/api/stocks/add", methods=["POST"])
@login_required
def add_stock():
    username = session.get("username")

    ticker = request.form["ticker"]
    company_name = alpaca.get_company_name(ticker)

    if company_name:
        watchlists.add_ticker(username, ticker, company_name)

    return redirect("/")

@app.route("/api/stocks/remove")
@login_required
def remove_stock():
    username = session.get("username")

    ticker = request.args.get("ticker")

    if ticker:
        watchlists.remove_ticker(username, ticker)

    return redirect("/")


if __name__ == "__main__":
    app.debug = True
    # app.secret_key = secrets.token_hex()
    app.secret_key = "a"
    app.run()