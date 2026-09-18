from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/", methods=["GET"])
def return_ip():
    client_info = {
        "client_ip": request.remote_addr,
        "user_agent": request.user_agent.string
    }
    return jsonify(client_info)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
