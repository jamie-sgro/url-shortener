from flask import Flask, request, redirect

from src.url_shortener.url_shortener import UrlShortener

app = Flask(__name__)


@app.route("/")
def home():
    return redirect("https://github.com/jamie-sgro/url-shortener", code=302)


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

@app.route("/api/v1/shortcode/get", methods=["GET"])
def shortcode_get():
    shortcode = request.args.get("shortcode")
    if type(shortcode) is not str:
        return "malformed shortcode", 400

    url_shortener = UrlShortener()
    url_model = url_shortener.get_url_from_shortcode(shortcode)

    if not url_model.status:
        return url_model.description, 400

    return url_model.value

# test12345
# SS0W5X