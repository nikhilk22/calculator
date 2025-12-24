from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "calculator",
        "version": "1.0.0"
    })

@app.route("/add", methods=["GET"])
def add():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify(result=a + b)
    except Exception as e:
        return jsonify(error="Invalid input"), 400

@app.route("/sub", methods=["GET"])
def subtract():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify(result=a - b)
    except Exception:
        return jsonify(error="Invalid input"), 400

@app.route("/mul", methods=["GET"])
def multiply():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify(result=a * b)
    except Exception:
        return jsonify(error="Invalid input"), 400

@app.route("/div", methods=["GET"])
def divide():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        if b == 0:
            return jsonify(error="Division by zero"), 400
        return jsonify(result=a / b)
    except Exception:
        return jsonify(error="Invalid input"), 400


if __name__ == "__main__":
    # Developer usually runs it like this locally
    app.run(debug=True)
