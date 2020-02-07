from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)


@app.route("/")
def index():
    print('are you even correct?')
    return render_template("index.html")


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201
    else:
        return jsonify({"about": "<h1>HELLO WORLD</h1>"})


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    print('Why is this shit confusing??')
    return jsonify({"result": num * 10})


if __name__ == '__main__':
    app.run(debug=True)
