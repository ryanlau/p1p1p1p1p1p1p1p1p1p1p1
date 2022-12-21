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

from api import alpaca, quotes, news, weather


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

    news_data = news.get_news_list()

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

    location = auth.get_location(username)
    weather_data = weather.get_next_five(location[0], location[1])

    print(weather_data)

    return render_template('dashboard.html', news_data=news_data, stock_data=stock_data, username=session['username'], quote=quote, todos=todos, wd=weather_data, city=location[2])

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
    zip = request.form.get('zip-code')

    if username and password and password_confirmation and zip:
        username = username.strip()
        password = password.strip()
        password_confirmation = password_confirmation.strip()
        zip = zip.strip()
        coords = weather.get_coords_from_zip(zip)

        if username == "":
            flash("username cannot be empty")

        if password == "":
            flash("password cannot be empty")

        if password != password_confirmation:
            flash("passwords do not match")
        
        if coords is None:
            flash("zip not valid")
            return redirect("/")

        if auth.check_username_availability(username):
            auth.add_new_user(username, password, coords["lat"], coords["lon"], coords["name"], zip)
            session["username"] = username
        else:
            flash("username not available")

    return redirect("/")


@app.route("/settings")
@login_required
def settings():
    location = auth.get_location(session["username"])
    return render_template('settings.html', zip=location[3])


@app.route("/settings/update", methods=["POST"])
@login_required
def update_settings():
    username = session.get("username")
    zip = request.form.get("zip")
    password = request.form.get("password")
    password_confirmation = request.form.get("password-confirmation")

    if zip:
        location = weather.get_coords_from_zip()

        if location:
            auth.update_user_location(username, location[0], location[1], location[2], location[3])
            flash("success!")
        else:
            flash("invalid zip code")

    if password and password_confirmation:
        if password == password_confirmation:
            auth.update_user_password(username, password)
            flash("success!")
        else:
            flash("passwords do not match")
    
    return redirect("/")


@app.route("/settings/delete")
@login_required
def delete_account():
    username = session.get("username")
    auth.delete_user(username)
    session.pop("username")
    return redirect("/")


@app.route("/weather")
@login_required
def weather_page():
    return render_template('weather.html')


@app.route("/news")
@login_required
def news_page():
    return render_template('news.html')


@app.route("/todos")
@login_required
def todo_page():
    return render_template('todos.html')


@app.route("/api/todos/update", methods=["POST"])
@login_required
def update_todo():
    username = session.get("username")

    _id = request.form.get("id").strip()
    status = 1 if request.form.get("status").strip() == "true" else 0

    todo.update_completion_status(_id, status)

    return ""


@app.route("/api/todos/add", methods=["POST"])
@login_required
def add_todo():
    username = session.get("username")

    item = request.form["todo"].strip()
    todo.add_todo(username, item, 0)

    return redirect("/")


@app.route("/api/todos/remove")
@login_required
def remove_todo():
    id = request.args.get("id").strip()
    todo.delete_todo(id)
    return redirect("/")


@app.route("/api/todos/remove_completed")
@login_required
def remove_all_completed_todos():
    username = session.get('username')
    todo.delete_all_completed_todos(username)
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


    auth.create_user_info_table()
    todo.create_todo_table()
    watchlists.create_watchlist_table()

    app.run()
