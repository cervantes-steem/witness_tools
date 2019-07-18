#!flask/bin/python
from flask import Flask, jsonify
from waitress import serve
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

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({sks})

@app.route('/api/get_debt_ratio', methods=['GET'])
def get_debt_ration():
    return jsonify(calc_debt_ratio.get_debt_ratio())

if __name__ == '__main__':
    #app.run(debug=False, port=8081)
    serve(app, host='0.0.0.0', port=8081)
