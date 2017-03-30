#!/usr/bin/env python3
from flask import Flask, request
from railway.route import Route
from vehicle.train import Train

app = Flask(__name__, static_url_path="/static")

train = Train()

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

@app.route("/start", methods=["POST"])
def start():
    if request.method == "POST":
        train.start(Route.convert_from_JSON(request.get_data(as_text=True)))

    return "Started", 200

if __name__ == "__main__":
    print('''
 ___   __    _  _______  ___   __    _  ___   _______  _______    _______  _______  ____   _______ 
|   | |  |  | ||       ||   | |  |  | ||   | |       ||       |  |       ||  _    ||    | |       |
|   | |   |_| ||    ___||   | |   |_| ||   | |_     _||    ___|  |____   || | |   | |   | |___    |
|   | |       ||   |___ |   | |       ||   |   |   |  |   |___    ____|  || | |   | |   |     |   |
|   | |  _    ||    ___||   | |  _    ||   |   |   |  |    ___|  | ______|| |_|   | |   |     |   |
|   | | | |   ||   |    |   | | | |   ||   |   |   |  |   |___   | |_____ |       | |   |     |   |
|___| |_|  |__||___|    |___| |_|  |__||___|   |___|  |_______|  |_______||_______| |___|     |___|  
                                                           
---------------------------------------------------------------------------------------------------
                                    A PROJECT BY OVERFLOW SIG
---------------------------------------------------------------------------------------------------
''')
    app.run(host="0.0.0.0")