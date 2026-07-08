import random
import string
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

shortened_urls = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        original_url = request.form['original_url']

        short_url = generate_short_url()

        shortened_urls[short_url] = original_url

        return render_template(
            'index.html',
            short_url=request.host_url + short_url
        )

    return render_template('index.html')


@app.route('/<short_url>')
def redirect_url(short_url):

    long_url = shortened_urls.get(short_url)

    if long_url:
        return redirect(long_url)

    return "URL not found", 404


if __name__ == "__main__":
    app.run(debug=True)