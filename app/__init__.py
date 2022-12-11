# FORTNITE: Ryan Lau, Craig Chen, Elizabeth Paperno, Hui Wang
# SoftDev
# p1: ohayo
# 2022-12-07
# time spent: 3.0 hrs


from flask import Flask, render_template, request, session
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/d")
def d():
    return render_template('dashboard.html')

@app.route("/register")
def register():
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
