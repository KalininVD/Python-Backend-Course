from datetime import datetime
from dotenv import dotenv_values
from flask import Flask, Response, jsonify, request

from controllers import operation


def get_port() -> int:
    """
    Get Flask app port from .env file.
    By default, port is 5000.

    Returns:
        port number (integer)
    """

    config = dotenv_values(".env")
    port = config.get("PORT", None)

    if port:
        return int(port)

    return 5000

def get_debug_mode() -> bool:
    """
    Get Flask app debug mode from .env file.
    By default, debug mode is disabled.

    Returns:
        whether debug mode is enabled or not (boolean)
    """

    config = dotenv_values(".env")
    debug_mode = config.get("DEBUG", None)

    if debug_mode:
        return bool(debug_mode)

    return False


# Initialize Flask app
app = Flask(__name__)


# Add the main route
@app.route("/")
def server_info() -> str:
    """
    Return information about the server.
    """

    return f"VDK server is running, current time is {datetime.now()}"

# Add the author route
@app.route("/author")
def author() -> Response:
    """
    Return information about the author of the server.
    """

    author = {
        "name": "VDK",
        "course": 2,
        "age": 18,
        "rating": 5,
    }

    return jsonify(author)

# Add the sum route
@app.route("/sum")
def runner() -> Response:
    """
    Return the result of operation defined in controllers.py.
    The result is a JSON object containing the operation's type and the result.
    """

    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    result = {
        'operation_description': operation.__doc__.replace('\n', ' ').strip() if operation.__doc__ else 'unknown operation',
        'operand_1': a,
        'operand_2': b,
        'result': operation(a, b)
    }

    return jsonify(result)


if __name__ == "__main__":
    # Run the app forever
    app.run(debug=get_debug_mode(), port=get_port())