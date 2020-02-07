import os

from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)


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

# sender email information configuration
app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
)

mymail = Mail(app)


@app.route('/send-mail')
def samplemail():
    # outgoing message
    msg = Message("Hello",
        sender=("Me", "manasadvr@gmail.com"),
        recipients=["16211a0543@bvrit.ac.in"],
        body="This is a test email I sent with Gmail and Python!")
    mymail.send(msg)
    if __name__ == '__main__':
         app.run()
    # message sent confirmation
    return "Your mail has been sent!"


if __name__ == '__main__':
    app.run(debug=True)
