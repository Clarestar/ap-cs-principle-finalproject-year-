from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome, to word guessing game!'

if __name__ == '_main_':
    app.run(host='localhost', port=2417)