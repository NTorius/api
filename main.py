from flask import Flask, jsonify
import json

from flask import Flask
app = Flask(__name__)

with open('api.json') as f:
   data = json.load(f)


@app.route("/api", methods=['GET'])
def get():
    return jsonify(data)




# print("hello w")

if __name__ == "__main__":
    app.run(debug=True)


