# FORTNITE: Ryan Lau, Craig Chen, Elizabeth Paperno, Hui Wang
# SoftDev
# p1: ohayo
# 2022-12-07
# time spent: 3.0 hrs


from flask import Flask, render_template, request, session, flash, redirect

import auth, todo, watchlists

import api.alpaca as alpaca

app = Flask(__name__) #create instance of class Flask


@app.route('/')
def index():
    if 'username' not in session:
        return render_template('login.html')
    
    # TODO: FETCH FOLLOWING DATA FROM DB
    stocks = [("AMZN", "Amazon.com, Inc."), ("AAPL", "Apple Inc. Common Stock")]
    snapshots = alpaca.get_snapshots([stock[0] for stock in stocks])
    for stock in stocks:
        snapshots[stock[0]]["name"] = stock[1]

    return render_template('dashboard.html', stock_data=snapshots)

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    info_correct = auth.check_creds(username, password)

    if info_correct:
        session['username'] = username
        session['user_id'] = auth.get_user_id(username)
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
def stocks():
    return render_template('stocks.html')


@app.route("/weather")
def weather():
    return render_template('weather.html')


@app.route("/news")
def news():
    return render_template('news.html')


@app.route("/todos")
def todo():
    return render_template('todos.html')


# @app.route("/api")


if __name__ == "__main__":
    app.debug = True
    app.secret_key = secrets.token_hex()

    app.run()
