from flask import Flask
from flask import request
from flask import jsonify
import functions
from functions import insert_attack

app = Flask(__name__)


@app.route("/insert-attack", methods=["POST"])
def insert_attack():
    data = request.get_json()
    try:
        functions.insert_attack(data['host'], data['port'])
        return jsonify({"action": "insert attack", "status": "OK"})
    except:
        return jsonify({"action": "insert attack", "status": "KO"}), 500


@app.route("/analyse-attacks")
def analyse_attacks():
    try:
        functions.analyse_attacks()
        return jsonify({"action": "analyse-attacks", "status": "OK"})
    except:
        return jsonify({"action": "analyse-attacks", "status": "KO"}), 500


if __name__ == '__main__':
    app.run()
