from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p> <p> new line</p>"

@app.route("/")
def index():
    return render_template('index.html')
    