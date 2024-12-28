from dotenv import dotenv_values
from flask import Flask, jsonify, request
from controllers import operation


def get_port() -> int:
    config = dotenv_values(".env")
    port = config.get("PORT", None)

    if port:
        return int(port)
    return 5000

def get_debug_mode() -> bool:
    config = dotenv_values(".env")
    debug_mode = config.get("DEBUG", None)

    if debug_mode:
        return bool(debug_mode)

    return False


app = Flask(__name__)


@app.route("/")
def server_info():
    return "My server"

@app.route("/author")
def author():
    author = {
        "name": "VDK",
        "course": 2,
        "age": 18,
    }

    return jsonify(author)

@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})


if __name__ == "__main__":
    app.run(debug=get_debug_mode(), port=get_port())