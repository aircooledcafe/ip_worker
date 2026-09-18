import asgiref.wsgi
from asgi_tools import Request as ASGIRequest  # or a WSGI-to-ASGI wrapper
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    # return render_template("index.html")
    return "Hello World Test"


@app.route("/ip", methods=["GET"])
def return_ip():
    client_info = {
        "client_ip": request.remote_addr,
        "user_agent": request.user_agent.string,
        "header": dict(request.headers),
    }
    return jsonify(client_info)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0")
asgi_app = asgiref.wsgi.WsgiToAsgi(app)


async def on_fetch(request, env):
    import open_async_endpoint  # adapter mechanism

    return await asgi_app(request)
