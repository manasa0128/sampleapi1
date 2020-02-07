from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)


@app.route("/")
def index():
    print('are you even correct?')
    return render_template("index.html")


app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='manasadvr@gmail.com',
    MAIL_PASSWORD='Magical@289',
)
mail = Mail(app)


@app.route('/test_path')
def test_path():
    return 'test_path'


@app.route('/send-mail')
def send_mail():
    try:
        msg = Message("This is an email that is being sent through flask application", sender="manasadvr@gmail.com",
                      recipients=["manasadvr@gmail.com"])
        msg.body = "Yo! This is crazy"
        mail.send(msg)
        return "mail sent succesfully"
    except Exception as e:
        return str(e)


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
