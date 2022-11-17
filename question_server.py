from flask import Flask
app_flask = Flask(__name__)
app = App()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"