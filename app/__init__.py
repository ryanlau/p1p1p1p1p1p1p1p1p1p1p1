# FORTNITE: Ryan Lau, Craig Chen, Elizabeth Paperno, Hui Wang
# SoftDev
# p1: ohayo
# 2022-12-07
# time spent: 3.0 hrs


from flask import Flask, render_template, request, session
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def login():

    return render_template('login.html')


@app.route("/register")       #assign fxn to route
def register():

    return render_template('register.html')
    
    
@app.route("/stocks")       #assign fxn to route
def stocks():

    return render_template('stocks.html')


@app.route("/weather")       #assign fxn to route
def weather():

    return render_template('weather.html')


@app.route("/news")       #assign fxn to route
def news():

    return render_template('news.html')


@app.route("/todo")       #assign fxn to route
def todo():

    return render_template('todo.html')


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
