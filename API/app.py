# API/app.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify, request
from Modules.web_scanner import scan_url
from Modules.network_monitor import monitor_network
from Modules.breach_checker import check_breach
from Modules.brute_force_tester import brute_force_test

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Aegis API!"})

@app.route("/scan", methods=["POST"])
def scan():
    data = request.json
    url = data.get("url", "")
    result = scan_url(url)
    return jsonify(result)

@app.route("/monitor", methods=["GET"])
def monitor():
    result = monitor_network()
    return jsonify(result)

@app.route("/breach", methods=["POST"])
def breach():
    data = request.json
    account = data.get("account", "")
    result = check_breach(account)
    return jsonify(result)

@app.route("/bruteforce", methods=["POST"])
def bruteforce():
    data = request.json
    target = data.get("target", "")
    result = brute_force_test(target)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
