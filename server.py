#!flask/bin/python

__author__ = "http://steemit.com/@cervantes"
__copyright__ = "Copyright (C) 2019 steem's @cervantes"
__license__ = "MIT"
__version__ = "1.0"


from flask import Flask, jsonify
import calc_debt_ratio

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.route('/api/get_debt_ratio', methods=['GET'])
def get_debt_ration():
    return jsonify(calc_debt_ratio.get_debt_ratio())

if __name__ == '__main__':
    app.run(debug=False)