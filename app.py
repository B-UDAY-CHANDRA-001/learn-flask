from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "helloWorld"

@app.route('/u')
def uday():
    return "hello Uday"


if __name__ == "main":
    app.run(debug=True)