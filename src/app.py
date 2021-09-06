from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/v1/url/add', methods=['POST'])
def api_all():
    return "/api/v1/url/add"