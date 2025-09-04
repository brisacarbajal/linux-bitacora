from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def main():
    return "<h1>PAKO </h1>"

@app.route('/saluda')
def saluda():
    return"<marquee><h2>Hola clase</h2></marquee>"

@app.route('/login')
def login():
    return render_template('login.html')

app.run()
    