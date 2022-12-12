# FORTNITE: Ryan Lau, Craig Chen, Elizabeth Paperno, Hui Wang
# SoftDev
# p1: ohayo
# 2022-12-07
# time spent: 3.0 hrs


from flask import Flask, render_template, request, session
# import api.alpaca as alpaca
app = Flask(__name__) #create instance of class Flask


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']

        return redirect(url_for('index'))
    return render_template('login.html')

@app.route("/d")
def d():
    stocks = [("AMZN", "Amazon.com, Inc."), ("AAPL", "Apple Inc. Common Stock")]
    snapshots = alpaca.get_snapshots([stock[0] for stock in stocks])
    for stock in stocks:
        snapshots[stock[0]]["name"] = stock[1]

    return render_template('dashboard.html', stock_data=snapshots)

@app.route("/register",methods=['POST'])
def register():
    if request.method == 'POST':    
        key = get_random_string()
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        
        command = f"insert into users values('{username}','{password}');"
        db.execute(command)
        
    file.commit()
    
    session["username"]= username
    session["password"]=password

    return render_template('register.html')
    
    
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


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
