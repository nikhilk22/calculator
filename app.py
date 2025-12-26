from flask import Flask, request, jsonify, render_template
import os
import logging
import signal
import sys

app = Flask(__name__)

# ---------------- DEVOPS CHANGE 1 ----------------
# Centralized logging (stdout → Docker/K8s logs)
logging.basicConfig(level=logging.INFO)


# ---------------- DEVOPS CHANGE 2 ----------------
# Health check endpoint (used by K8s, LB, monitoring)
@app.route("/health")
def health():
        return {"status": "UP"}, 200

# ------app route -----#    

@app.route("/")
def home():
    return render_template("index.html")


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


# ---------------- DEVOPS CHANGE 3 ----------------
# Graceful shutdown for containers
def shutdown_handler(sig, frame):
    logging.info("Shutting down gracefully...")
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)

# ---------------- DEVOPS CHANGE 4 ----------------
# Config via environment variables
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
