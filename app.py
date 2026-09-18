from flask import Flask, jsonify, render_template, request
from workers import wsgi

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
    #return "Hello World Test"


@app.route("/ip", methods=["GET"])
def return_ip():
    client_info = {
        "client_ip": request.headers.get("Cf-Connecting-Ip"),
        "user_agent": request.headers.get("User-Agent"),
        "x-real-ip": request.headers.get("X-Real-Ip"),
        "header": dict(request.headers),
    }
    return jsonify(client_info)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0")
Default = wsgi.entrypoint(app)
