from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello From Flask"

app.run(port=5000, debug=True)