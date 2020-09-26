#!flask/bin/python

__author__ = "http://hive.blog/@cervantes"
__copyright__ = "Copyright (C) 2019 hive's @cervantes"
__license__ = "MIT"
__version__ = "1.0"


from flask import Flask, jsonify
from waitress import serve
import calc_debt_ratio

app = Flask(__name__)


@app.route('/api/get_debt_ratio', methods=['GET'])
def get_debt_ration():
    return jsonify(calc_debt_ratio.get_debt_ratio())

if __name__ == '__main__':

    serve(app, host='0.0.0.0', port=8081)
