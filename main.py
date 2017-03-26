#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/map")
def map():
    file = open("./data/map.json", "r")
    json = file.read()
    file.close()

    response = app.make_response(json)

    # Specify content & mime type
    response.headers["Content-Type"] = "application/json"
    response.mimetype = "application/json"

    return response

if __name__ == "__main__":
    app.run()