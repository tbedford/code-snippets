from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/a", methods=['GET'])
def a():
    m = [1,2,3]
    return json.dumps(m)

@app.route("/b", methods=['GET'])
def b():
    m = [1,2,3]
    return jsonify(m) 

@app.route("/c", methods=['GET'])
def c():
    user1 = {'name': 'Fred', 'age': 62}
    user2 = {'name': 'Jim', 'age': 24}
    users = [user1, user2]
    return jsonify(users) 

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
