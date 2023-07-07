from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/code')
def code():
    return "route for code"


if __name__ == '__main__':
    app.run(debug = True)