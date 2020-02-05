from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


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
