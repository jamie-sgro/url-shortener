from flask import Flask, request

from src.url_shortener.url_shortener import UrlShortener

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/v1/url/add", methods=["POST"])
def url_add():
    url = request.args.get("url")
    if type(url) is not str:
        return "malformed url", 400

    url_shortener = UrlShortener()
    shortcode_model = url_shortener.submit_url_and_get_shortcode(url)
    
    if not shortcode_model.status:
        return shortcode_model.description, 400

    return shortcode_model.value
