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

from api import alpaca, quotes


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

    stocks = watchlists.get_watchlist(username)

    stock_data = {}
    if stocks:
        stock_data = alpaca.get_snapshots([stock[0] for stock in stocks])
        bars = alpaca.get_daily_bars([stock[0] for stock in stocks])

        for stock in stocks:
            stock_data[stock[0]]["name"] = stock[1]
            stock_data[stock[0]]["bars"] = bars.get(stock[0])

    quote = quotes.get_qotd()

    todos = todo.get_all_todos(username)
    print(todos)

    return render_template('dashboard.html', stock_data=stock_data, username=session['username'], quote=quote, todos=todos)

@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    info_correct = auth.check_creds(username, password)

    if info_correct:
        session['username'] = username
    else:
        flash("invalid username or password")

    return redirect("/")


@app.route("/logout")
@login_required
def logout():
    session.pop('username', None)
    return redirect("/")


@app.route("/register",methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    password_confirmation = request.form.get('password-confirmation')

    if username and password and password_confirmation:
        username = username.strip()
        password = password.strip()
        password_confirmation = password_confirmation.strip()

        if username == "":
            flash("username cannot be empty")

        if password == "":
            flash("password cannot be empty")

        if password != password_confirmation:
            flash("passwords do not match")
        
        if auth.check_username_availability(username):
            auth.add_new_user(username, password)
            session["username"] = username
        else:
            flash("username not available")

    return redirect("/")
    
    
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
def todo_page():
    return render_template('todos.html')


@app.route("/api/todo/add", methods=["POST"])
@login_required
def add_todo():
    username = session.get("username")

    item = request.form["todo"].strip()
    todo.add_todo(username, item, 0)

    return redirect("/")

@app.route("/api/stocks/add", methods=["POST"])
@login_required
def add_stock():
    username = session.get("username")

    ticker = request.form["ticker"].upper()
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
